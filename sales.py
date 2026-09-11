from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "Sample - Superstore.csv"

def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    df = pd.read_csv(path, encoding="latin1").drop_duplicates().copy()
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["YearMonth"] = df["Order Date"].dt.to_period("M").dt.to_timestamp()
    return df

def monthly_sales(df):
    return df.groupby("YearMonth")["Sales"].sum().sort_index()

def category_analysis(df):
    return df.groupby("Category")[["Sales", "Profit"]].sum().sort_values("Profit", ascending=False).reset_index()

def subcategory_analysis(df):
    return df.groupby("Sub-Category")[["Sales", "Profit"]].sum().sort_values("Profit").reset_index()

def customer_rfm(df):
    today = df["Order Date"].max()
    rfm = df.groupby("Customer Name").agg(
        Recency=("Order Date", lambda x: (today - x.max()).days),
        Frequency=("Order ID", "count"),
        Monetary=("Sales", "sum"),
    )
    def segment(row):
        if row["Monetary"] > 5000 and row["Frequency"] > 5:
            return "High Value"
        if row["Monetary"] < 2000:
            return "Medium Value"
        return "Low Value"
    rfm["Segment"] = rfm.apply(segment, axis=1)
    return rfm.reset_index()

def create_charts(df, output_dir=BASE_DIR / "outputs"):
    output_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")
    series = monthly_sales(df)
    plt.figure(figsize=(12, 5))
    plt.plot(series.index, series.values)
    plt.title("Monthly Sales Trend")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / "monthly_sales_trend.png", dpi=150)
    plt.close()
    cat = category_analysis(df)
    for metric, filename, title in [
        ("Sales", "sales_by_category.png", "Sales by Category"),
        ("Profit", "profit_by_category.png", "Profit by Category"),
    ]:
        plt.figure(figsize=(8, 5))
        sns.barplot(data=cat, x="Category", y=metric)
        plt.title(title)
        plt.tight_layout()
        plt.savefig(output_dir / filename, dpi=150)
        plt.close()
    sub = subcategory_analysis(df)
    plt.figure(figsize=(9, 6))
    sns.barplot(data=sub, x="Profit", y="Sub-Category")
    plt.title("Profit by Sub-Category")
    plt.tight_layout()
    plt.savefig(output_dir / "profit_by_subcategory.png", dpi=150)
    plt.close()
    plt.figure(figsize=(9, 6))
    sns.scatterplot(data=df, x="Discount", y="Profit", hue="Category")
    plt.title("Discount vs Profit by Category")
    plt.tight_layout()
    plt.savefig(output_dir / "discount_vs_profit.png", dpi=150)
    plt.close()

def main():
    df = load_data()
    print("Rows:", f"{len(df):,}")
    print("Total sales:", f"$"+f"{df['Sales'].sum():,.2f}")
    print("Total profit:", f"$"+f"{df['Profit'].sum():,.2f}")
    print("Average discount:", f"{df['Discount'].mean():.2%}")
    print(category_analysis(df).to_string(index=False))
    print(customer_rfm(df)["Segment"].value_counts().to_string())
    create_charts(df)

if __name__ == "__main__":
    main()
