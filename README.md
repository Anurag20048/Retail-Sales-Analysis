# 📊 Retail Sales Analysis & Customer Insights

An end-to-end retail analytics project built with Python. It analyzes sales trends, profitability, discount impact, product performance, and customer purchasing behavior, with an interactive Streamlit dashboard.

## What this project answers

- How are sales changing over time?
- Which categories and sub-categories drive profit?
- Which products or sub-categories are loss-making?
- How does discounting affect profit?
- Which customers generate the most revenue?
- Which customers are high-value based on RFM analysis?

## Key Features

- Portable, project-relative dataset loading
- Data cleaning and duplicate removal
- Date parsing and time-series feature engineering
- Monthly sales trend analysis
- Category and sub-category profitability analysis
- Discount vs. profit analysis
- Top-customer analysis
- RFM-style customer segmentation
- Interactive Streamlit dashboard
- Automated regression tests
- GitHub Actions CI

## Technology Stack

| Area | Tools |
|---|---|
| Language | Python |
| Data | Pandas, NumPy-compatible workflows |
| Visualization | Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Testing | Pytest |
| CI | GitHub Actions |

## Project Structure

```
Retail-Sales-Analysis/
├── Sample - Superstore.csv
├── sales.py
├── app.py
├── requirements.txt
├── tests/
│   └── test_sales.py
├── outputs/
└── README.md
```

## Run locally

Clone the repository and install dependencies:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Run the analysis:

```bash
python sales.py
```

Launch the interactive dashboard:

```bash
streamlit run app.py
```

Run tests:

```bash
python -m pytest -q
```

## Dashboard

The Streamlit dashboard provides:

- Total sales, profit, orders, and customer KPIs
- Monthly sales trend
- Sales and profit by category
- Profit by sub-category
- Discount/profit exploration
- Customer RFM segmentation
- Top customer table
- Business insights

## Analysis Highlights

The project investigates the relationship between sales volume and profitability rather than treating revenue as the only success metric. It also evaluates the effect of discounting and uses customer purchasing behavior to identify higher-value segments.

The exact results are generated directly from the included dataset when the analysis pipeline runs.

## Validation

The repository includes automated tests covering:

- Dataset loading
- Date parsing
- Monthly aggregation
- Category/sub-category analysis
- RFM segmentation

GitHub Actions runs the regression suite against the repository dataset.

## Screenshots

Existing dashboard and analysis screenshots are retained below.

<img width="1493" height="708" alt="Retail analysis dashboard" src="https://github.com/user-attachments/assets/96d21b02-934c-4586-a4db-aec7e86e5aa6" />

<img width="992" height="708" alt="Retail analysis visualization" src="https://github.com/user-attachments/assets/8a660cf0-59a4-4126-8dcb-24ba0c0f9b8f" />

<img width="993" height="703" alt="Retail analysis visualization" src="https://github.com/user-attachments/assets/0e00d516-5610-4e13-9763-13e6cf3c5a35" />

<img width="1920" height="1080" alt="Retail analysis dashboard" src="https://github.com/user-attachments/assets/b4d3fd6b-6916-4dba-83c2-9d618d34b5b1" />

<img width="1002" height="709" alt="Retail analysis visualization" src="https://github.com/user-attachments/assets/57adad80-a60f-4ee6-a4b3-ff8d5de3a4b9" />

<img width="1920" height="1080" alt="Retail analysis dashboard" src="https://github.com/user-attachments/assets/24836a60-7173-48d0-91f6-c925b028b04e" />

## Business Recommendations

- Reduce unnecessary discounting where it damages margins.
- Prioritize retention of high-value customers.
- Investigate consistently loss-making sub-categories.
- Use both revenue and profit when evaluating product performance.
- Use customer segmentation to target retention and promotional activity.

## Author

**Anurag Pareek**
