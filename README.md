# 📊 Retail Sales Analysis & Customer Insights

> An end-to-end data analytics project that transforms retail transaction data into insights on sales performance, profitability, discounts, products, and customer behavior.

## 🎯 Project Overview

This project analyzes the **Sample Superstore** retail dataset to understand how sales and profit change across time, product categories, customer segments, and discount levels.

The analysis follows a complete data analytics workflow: data preparation, exploratory analysis, KPI development, profitability analysis, customer segmentation, visualization, and an interactive Streamlit dashboard.

The goal is to move beyond descriptive charts and answer practical business questions such as:

- Which categories and sub-categories contribute the most revenue and profit?
- How do discounts affect profitability?
- Which customers contribute the highest value?
- What are the major sales and profit trends over time?
- Which customer groups can be prioritized for retention and growth?

## 📌 Business Objectives

1. Measure overall sales and profitability performance.
2. Identify high-performing and under-performing product categories.
3. Analyze the relationship between discounts and profit.
4. Understand customer purchasing behavior.
5. Identify valuable customer segments using RFM-style analysis.
6. Present findings through an interactive dashboard.

## 🔄 Analysis Workflow

```text
Retail Transaction Data
        ↓
Data Cleaning & Validation
        ↓
Feature Engineering
        ↓
Exploratory Data Analysis
        ↓
Sales & Profitability Analysis
        ↓
Customer Segmentation
        ↓
Business Insights
        ↓
Interactive Streamlit Dashboard
```

## 🧹 Data Preparation

The project includes:

- Duplicate-record handling
- Date parsing and validation
- Derived time-based features
- Sales and profit aggregation
- Category and sub-category grouping
- Customer-level aggregation
- Discount and profitability analysis
- Preparation of data for dashboard reporting

## 📈 Key Analysis Areas

### Sales Performance
- Monthly and yearly sales trends
- Category and sub-category performance
- Product-level contribution
- Customer sales contribution

### Profitability
- Profit by category and sub-category
- Discount versus profit analysis
- Identification of profitable and under-performing segments
- Sales-to-profit comparison

### Customer Analytics
- Top customers by sales
- Customer purchase behavior
- RFM-style customer segmentation
- Identification of high-value customer groups

## 📊 Dashboard

The Streamlit dashboard provides an interactive view of the analysis with:

- Sales KPIs
- Profit KPIs
- Category performance
- Sales trends
- Profitability analysis
- Customer insights
- Interactive filters and visualizations

## 🛠️ Technology Stack

| Area | Technology |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Testing | Pytest |
| Version Control | Git / GitHub |
| Dataset | Sample Superstore |

## 📁 Project Structure

```text
Retail-Sales-Analysis/
├── Sample - Superstore.csv
├── sales.py
├── app.py
├── requirements.txt
├── tests/
├── outputs/
└── README.md
```

## ▶️ Run the Project

### Clone the repository

```bash
git clone https://github.com/Anurag20048/Retail-Sales-Analysis.git
cd Retail-Sales-Analysis
```

### Create a virtual environment

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the analysis

```bash
python sales.py
```

### Launch the dashboard

```bash
streamlit run app.py
```

## 🧪 Running Tests

```bash
python -m pytest -q
```

## 💡 Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory Data Analysis
- KPI development
- Time-series analysis
- Profitability analysis
- Customer segmentation
- Data visualization
- Dashboard development
- Python analytics
- Business-oriented data storytelling
- Automated testing

## 🔮 Future Enhancements

- Add automated data-refresh workflows
- Expand customer segmentation
- Add additional profitability KPIs
- Add advanced dashboard filtering
- Deploy the Streamlit dashboard

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss the proposed improvement.

## 📄 License

See the `LICENSE` file for licensing information.

## 👤 Author

**Anurag Pareek**

- GitHub: https://github.com/Anurag20048
