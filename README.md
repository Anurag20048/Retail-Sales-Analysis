# Retail Sales Analysis & Customer Insights

> An end-to-end Python analytics project that explores retail sales, profitability, discount impact, product performance, and customer purchasing behavior through an interactive dashboard.

## 🚀 Overview
This project transforms retail transaction data into business-focused insights. The workflow covers data cleaning, time-series analysis, profitability analysis, customer segmentation, RFM-style analysis, and interactive visualization through Streamlit.

## 📸 Dashboard
The repository includes dashboard and analysis screenshots demonstrating the interactive Streamlit experience.

## ✨ Features
- Data cleaning and duplicate handling
- Date parsing and feature engineering
- Monthly sales trend analysis
- Category and sub-category profitability
- Discount versus profit analysis
- Top-customer analysis
- RFM-style customer segmentation
- Sales and profit KPIs
- Interactive Streamlit dashboard
- Automated regression tests
- GitHub Actions CI

## 🛠️ Tech Stack
Python · Pandas · NumPy · Matplotlib · Seaborn · Streamlit · Pytest · GitHub Actions

## 📦 Installation
```bash
git clone https://github.com/Anurag20048/Retail-Sales-Analysis.git
cd Retail-Sales-Analysis
python -m venv .venv
```

Windows:
```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## ▶️ Usage
Run the analysis:
```bash
python sales.py
```

Launch the dashboard:
```bash
streamlit run app.py
```

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

## 🔧 Configuration
The project uses the included dataset and repository-relative paths.

## 🧪 Running Tests
```bash
python -m pytest -q
```

## 🗺️ Roadmap
- [ ] Add automated data-quality reporting
- [ ] Expand customer segmentation
- [ ] Add dashboard deployment
- [ ] Add additional profitability metrics

## 🤝 Contributing
Pull requests are welcome. For major changes, open an issue first.

## 📄 License
See the `LICENSE` file.

## 👤 Author
**Anurag Pareek**
- GitHub: https://github.com/Anurag20048
