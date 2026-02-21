# 📊 Telecom Customer Churn & Revenue Risk Analysis

## 📌 Project Overview

This project analyzes telecom customer churn behavior to identify high-risk customer segments and quantify revenue exposure.

Using **Python (Pandas)** for data analysis and **Power BI** for visualization, this project transforms raw telecom data into actionable business insights that support customer retention strategy and revenue protection.

The goal:
> Identify churn drivers, calculate revenue at risk, and simulate retention impact.

---

# 🎯 Business Objectives

- Measure churn rate and revenue loss
- Identify high-risk customer segments
- Quantify revenue exposure by contract type
- Analyze service-level churn drivers
- Simulate revenue recovery through retention strategy

---

# 📊 Key Business Metrics

- **Total Revenue from Churned Customers:** ₹8,217,301.91  
- **Average Revenue per Churned Customer:** ₹2,474.35  
- **Month-to-Month Customer Count:** 2,595  
- **Month-to-Month Revenue at Risk:** ₹6,358,469.39  
- **Potential Customers Saved (25% Retention Simulation):** 648+  
- **Potential Revenue Recovery:** ₹1,589,617.35  

---

# 🔎 Key Insights

## 1️⃣ Contract Type Risk

- Month-to-Month contracts contribute the highest revenue risk.
- Revenue exposure from Month-to-Month customers: ₹6.35M+
- Long-term contracts show significantly lower churn impact.

---

## 2️⃣ Internet Service Risk

- **Fiber Optic customers have the highest churn rate (61.31%)**
- DSL churn rate: 36.51%
- Customers without internet: 35.55%

---

## 3️⃣ Tech Support Impact

- Customers without Tech Support:
  - **53.61% churn rate**
- Customers with Tech Support:
  - 32.86% churn rate

Strong evidence that Tech Support reduces churn probability.

---

## 4️⃣ Payment Method Analysis

Churn rate across payment methods remains similar (~47–48%), indicating payment type is not a primary churn driver.

---

# 📈 Power BI Dashboard Structure

## Page 1 – Executive Overview
- KPI Cards (Revenue at Risk, Avg Revenue per Churn, Potential Revenue Recovery)
- Revenue Lost by Contract Type
- Churn Rate by Contract Type
- Churn vs Non-Churn

<img width="985" height="566" alt="executive_overview" src="https://github.com/user-attachments/assets/304ed6a8-dd4f-4fc4-bab3-882efe4d4a81" />

## Page 2 – Root Cause Deep Dive
- Revenue Lost by Internet Service
- Revenue Lost by Tech Support
- Churn Rate by Tenure Month
- Churn Rate by Contract Type and Internet Service

<img width="978" height="558" alt="root_cause" src="https://github.com/user-attachments/assets/22659429-9222-46c2-8c1c-3f1fbbc0c6d7" />

## Page 3 – Strategic Simulation (Decision Dashboard)
- What-If Slicer -- Retention Simulation (25% scenario)
- KPI Cards (MTM Revenue Lost, Customers Saved, Revenue Saved, New Revenue Loss)
- Comparison Chart (Current Revenue Loss vs After Retention Strategy)

  <img width="978" height="559" alt="strategic_simulation" src="https://github.com/user-attachments/assets/5d75270c-9ddc-4d80-b83a-88009f2df547" />
  
---

# 🧮 Retention Simulation Logic

Assumption:
If 25% of high-risk Month-to-Month customers are retained:

- Customers saved: 648+
- Revenue recovered: ₹1,589,617.35

This provides a quantifiable retention strategy for decision-makers.

---

# 🛠️ Tools & Technologies Used

- **Python (Pandas)**  
  - Data cleaning  
  - Grouping & aggregation  
  - Churn rate calculations  
  - Revenue risk computation  
  - Retention simulation  

- **Power BI**  
  - Data modeling  
  - DAX measures  
  - KPI dashboards  
  - Interactive drill-down analysis  

---

# 📂 Repository Structure
```
Telecom-Customer-Churn-Analysis
│
├── telecom_customer_churn_dataset.csv
├── churn_analysis.py
├── telecom_customer_churn_dashboard.pbix
├── screenshots/
│   └── executive_overview.png
│   └── root_cause.png
│   └── strategic_simulation.png
└── README.md
```


---

# 🧠 Business Recommendations

- Convert Month-to-Month customers into long-term contracts
- Offer bundled Tech Support to reduce churn risk
- Improve Fiber Optic service quality to reduce dissatisfaction
- Run targeted retention campaigns for high-revenue customers

---

# 👤 Author

**Manish Sharma**  
Aspiring Data Analyst | Business Intelligence Enthusiast  

LinkedIn: https://www.linkedin.com/in/manish-sharma-552b892b7/
GitHub: https://github.com/ms08724919483-ops 


