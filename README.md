# 📊 Vendor Performance Analysis Dashboard

## 🚀 Overview
This project is an **end-to-end data analytics pipeline** built to analyze vendor performance using purchase, sales, and inventory data.

It demonstrates the complete data workflow:
- Data Ingestion  
- Data Storage  
- Data Transformation  
- Feature Engineering  
- Data Visualization  

The final output is an **interactive Power BI dashboard** that provides actionable business insights.

---

## 🧠 Problem Statement
Organizations often struggle to evaluate vendor performance due to fragmented data across multiple sources.

This project solves that problem by:
- Consolidating vendor-related data  
- Measuring profitability and efficiency  
- Identifying top-performing and underperforming vendors  

---

## ⚙️ Tech Stack
- **Programming:** Python  
- **Libraries:** Pandas, SQLAlchemy  
- **Database:** SQLite  
- **Querying:** SQL (CTEs, Joins, Aggregations)  
- **Visualization:** Power BI  
- **Logging:** Python Logging Module  

---

## 🏗️ Project Architecture

### 🔹 1. Data Ingestion
- Reads multiple CSV files from the `Data/` folder  
- Loads data into SQLite database (`inventory.db`)  
- Logs ingestion process and execution time  

### 🔹 2. Data Processing & Transformation
- Merges multiple datasets:
  - Purchases  
  - Sales  
  - Vendor Invoices  
  - Purchase Prices  
- Uses **SQL CTEs** for optimized queries  
- Creates a unified vendor summary  

### 🔹 3. Data Cleaning & Feature Engineering
- Handles missing values  
- Standardizes data types  
- Creates key business metrics:
  - **Gross Profit**  
  - **Profit Margin (%)**  
  - **Stock Turnover**  
  - **Sales-to-Purchase Ratio**  

### 🔹 4. Data Visualization
- Built using **Power BI**  
- Provides:
  - Vendor comparison  
  - Profitability insights  
  - Sales trends  

---

## 📈 Key Insights Generated
- Top-performing vendors based on profit  
- Vendors with low or negative margins  
- Inventory efficiency using stock turnover  
- Sales vs purchase behavior analysis  

---

## 📂 Project Structure
```bash
├── Data/
├── Logs/
├── ingestion_db.py
├── get_vendor_summary.py
├── Vendor Performance Dashboard.pbix
├── notebooks/
└── README.md
```
---

## ▶️ How to Run

### 1️⃣ Install Dependencies
```bash
pip install pandas sqlalchemy
```
### 2️⃣ Run Data Ingestion
```bash
python ingestion_db.py
```
### 3️⃣ Generate Vendor Summary
```bash
python get_vendor_summary.py
```
### 4️⃣ Open Dashboard
Open the .pbix file in Power BI Desktop

---

## 📁 Dataset

This repository includes a sample dataset for demonstration purposes.

To run the project with your own data, place CSV files inside the Data/ folder with the following structure:
```bash
├──purchases.csv
├──sales.csv
├──vendor_invoice.csv
└──purchase_prices.csv
```
⚠️ Note: The pipeline is designed to handle large-scale datasets efficiently.

---

## 📊 Business Metrics
- Gross Profit = Total Sales - Total Purchase
- Profit Margin (%) = (Profit / Sales) × 100
- Stock Turnover = Sales Quantity / Purchase Quantity
- Sales-to-Purchase Ratio = Sales / Purchase

---

## 💡 Key Features

#### ✔ End-to-end data pipeline
#### ✔ Automated data ingestion
#### ✔ Advanced SQL transformations (CTEs, joins)
#### ✔ Business-focused KPI generation
#### ✔ Interactive Power BI dashboard
#### ✔ Logging system for monitoring

---

## 🚀 Future Improvements
- Deploy pipeline on cloud (AWS / GCP)
- Build interactive dashboard using Streamlit
- Add real-time data processing
- Implement predictive analytics (vendor forecasting)

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐ on GitHub!
