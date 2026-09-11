from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sales import category_analysis, customer_rfm, load_data, monthly_sales, subcategory_analysis
DATA = Path(__file__).resolve().parents[1] / "Sample - Superstore.csv"

def test_dataset_loads():
    df = load_data(DATA)
    assert len(df) > 0
    assert df["Order Date"].notna().all()
    assert df["Ship Date"].notna().all()

def test_monthly_sales():
    result = monthly_sales(load_data(DATA))
    assert len(result) > 0
    assert result.index.is_monotonic_increasing

def test_analysis_columns():
    df = load_data(DATA)
    assert set(["Category","Sales","Profit"]).issubset(category_analysis(df).columns)
    assert set(["Sub-Category","Sales","Profit"]).issubset(subcategory_analysis(df).columns)

def test_rfm():
    rfm = customer_rfm(load_data(DATA))
    assert set(["Customer Name","Recency","Frequency","Monetary","Segment"]).issubset(rfm.columns)
    assert rfm["Segment"].notna().all()
