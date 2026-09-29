# 🛒 E-commerce Sales Analysis

An end-to-end **Python Data Analyst portfolio project** analyzing e-commerce transactions to identify revenue trends, category performance, top products and regional sales patterns.

## 🎯 Business Objective

Convert raw sales transaction data into meaningful business insights that can support decisions around products, regions, customers and sales performance.

## 🧰 Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- CSV

## 📁 Project Structure

```text
Ecommerce-Sales-Analysis/
├── data/
│   ├── raw/ecommerce_sales.csv
│   └── processed/cleaned_sales.csv
├── notebooks/ecommerce_sales_analysis.ipynb
├── src/data_analysis.py
├── outputs/
│   ├── monthly_revenue.png
│   ├── category_revenue.png
│   ├── top_10_products.png
│   └── region_revenue.png
├── README.md
├── requirements.txt
└── .gitignore
```

## 🔄 Analysis Workflow

**Raw Data → Data Validation → Data Cleaning → EDA → KPI Analysis → Visualization → Business Insights**

## 🧹 Data Cleaning

- Removed duplicate records
- Converted order dates to datetime
- Handled missing regions and payment methods
- Imputed missing discounts using the median
- Converted numeric fields to appropriate types
- Created monthly analysis fields
- Filtered completed orders for revenue KPIs

## 📊 Key KPIs

| KPI | Result |
|---|---:|
| Total Revenue | ₹54,111,495.64 |
| Completed Orders | 4,405 |
| Average Order Value | ₹12,284.11 |
| Unique Customers | 894 |
| Total Units Sold | 8,376 |
| Cancellation Rate | 6.80% |
| Return Rate | 5.10% |

## 🔎 Key Findings

- **Highest revenue month:** 2025-09, with approximately **₹5,535,347** revenue.
- **Top revenue category:** Electronics.
- **Top revenue region:** South.
- **Top revenue-generating product:** Headphones.
- Performance can also be segmented by channel, payment method and customer.

## 📈 Visualizations

### Monthly Revenue
![Monthly Revenue](outputs/monthly_revenue.png)

### Revenue by Category
![Category Revenue](outputs/category_revenue.png)

### Top 10 Products
![Top Products](outputs/top_10_products.png)

### Revenue by Region
![Regional Revenue](outputs/region_revenue.png)

## ▶️ How to Run

```bash
git clone https://github.com/YOUR_USERNAME/Ecommerce-Sales-Analysis.git
cd Ecommerce-Sales-Analysis
pip install -r requirements.txt
jupyter notebook
```

Open:

`notebooks/ecommerce_sales_analysis.ipynb`

## 💼 Interview Talking Points

This project demonstrates my ability to:

- Work with raw transactional data
- Perform data validation and cleaning
- Use Pandas for analysis
- Calculate business KPIs
- Perform exploratory data analysis
- Create business-focused visualizations
- Translate data into actionable insights
- Structure a reproducible analytics project

## 🚀 Future Enhancements

- Add SQL analysis
- Build an interactive Power BI dashboard
- Add customer segmentation
- Perform RFM analysis
- Add cohort analysis
- Automate the reporting pipeline

---

**Author:** Swatantra Pratap Singh  
**Role:** Data Analyst
