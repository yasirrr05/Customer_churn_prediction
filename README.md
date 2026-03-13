# 📉 Customer Churn Prediction & Analysis

> End-to-end data analysis project using SQL, Python (EDA + Machine Learning), and Power BI to predict customer churn, quantify revenue at risk, and deliver actionable retention strategies for a telecom company.

<div align="center">

![Power BI Dashboard](charts/powerbi_dashboard.png)

</div>

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-blue.svg)](https://www.postgresql.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange.svg)](https://scikit-learn.org/)
[![PowerBI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![Excel](https://img.shields.io/badge/Microsoft-Excel-green.svg)](https://microsoft.com/excel)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)]()

---

## 🎯 Project Overview

End-to-end data analysis and machine learning project analyzing 7,043 telecom customer records to identify churn drivers, predict at-risk customers, and quantify revenue impact. The project spans the full analyst workflow — from Excel exploration and SQL analysis to Python machine learning and Power BI dashboard.

**📖 [Read Full Analysis Report](./churn_analysis.md)**

Report Includes:
- Executive summary with key findings
- SQL business intelligence analysis (6 queries)
- Python EDA with 5 statistical visualizations
- ML model comparison (Logistic Regression vs Random Forest)
- Revenue at risk quantification
- Strategic retention recommendations with ROI estimates
- Complete SQL query documentation

---

## 📊 Project Highlights

**6 Interactive Visualizations:**

1. **📊 Overall Churn Rate KPI** — 26.54% headline metric in red
2. **📋 Churn Rate by Contract Type** — Traffic light bar chart (red/orange/green)
3. **📈 Churn Rate by Tenure Group** — Declining line chart showing loyalty effect
4. **🍩 Customers by Value Segment** — Donut chart (High/Medium/Low value)
5. **📊 Top Churn Reasons** — Horizontal bar chart ranked by frequency
6. **🔽 Contract Type Slicer** — Interactive filter for all visuals

**Interactive Features:**
- Click any contract type in the slicer → all 5 charts update dynamically
- Hover over any chart element for detailed tooltips
- Cross-filter between visuals for drill-down analysis

**Key Findings:**
- 🚨 **26.54% overall churn rate** — 1 in 4 customers leaving, above industry benchmark
- 📋 **Month-to-month contracts** churn at **42.7%** — 15x higher than two-year contracts
- 💰 **$139,130 monthly revenue at risk** ($1.67M annualized) from churning customers
- ⏰ **First 12 months are critical** — new customers churn at 47.4% vs 9.5% for loyal customers
- 🖥️ **Fiber optic customers** churn at 41.9% despite paying premium prices
- 🤖 **ML model achieves 80.6% accuracy** identifying at-risk customers before they leave

**Business Impact:**
- Quantified **$1.67M annual revenue at risk** from current churn rate
- Built predictive model identifying **top 3 churn drivers** (monthly charges, tenure, contract type)
- Discovered **support quality is #1 churn reason** — fixable without product changes
- Recommended retention strategies with projected **ROI of 300-800%**

**Tools Used:** 
SQL (PostgreSQL) • Excel • Python (pandas, matplotlib, seaborn, scikit-learn) • Power BI

---

## 🎯 Business Questions Answered

✅ What is the overall customer churn rate?
✅ Which contract types have the highest churn risk?
✅ How much revenue is being lost to churn monthly?
✅ Which customers are most likely to churn next?
✅ What are the top reasons customers leave?
✅ Which customer tenure group needs immediate attention?
✅ What retention strategies will deliver the highest ROI?

---

## 💡 Key Insights

### Churn Overview
- **Overall Churn Rate:** 26.54% (1,869 out of 7,043 customers)
- **Industry Benchmark:** ~20% — this company is **6.5 points above average**
- **Monthly Revenue Lost:** $139,130 to churning customers
- **Annualized Revenue at Risk:** $1,669,560

### Contract Type Analysis
| Contract | Total Customers | Churned | Churn Rate | Risk Level |
|----------|----------------|---------|------------|------------|
| Month-to-month | 3,875 | 1,655 | **42.71%** | 🚨 Critical |
| One year | 1,473 | 166 | **11.27%** | ⚠️ Moderate |
| Two year | 1,695 | 48 | **2.83%** | ✅ Low |

**Insight:** Month-to-month customers churn at **15x the rate** of two-year contract customers. Converting just 10% of monthly customers to annual contracts could save ~$1.6M annually.

### Tenure Analysis
| Tenure Group | Total Customers | Churned | Churn Rate |
|-------------|----------------|---------|------------|
| 0-12 Months | 2,186 | 1,037 | **47.44%** 🚨 |
| 13-24 Months | 1,024 | 294 | **28.71%** ⚠️ |
| 25-48 Months | 1,594 | 325 | **20.39%** ⚠️ |
| 49+ Months | 2,239 | 213 | **9.51%** ✅ |

**Insight:** Nearly half of all new customers (0-12 months) churn. The first year is the single most critical retention window.

### Top Churn Reasons
1. **Attitude of support person** — 192 customers (10.27%) 🔧 Fixable
2. **Competitor offered higher download speeds** — 189 customers (10.11%) 📶
3. **Competitor offered more data** — 162 customers (8.67%) 📱
4. **Don't know** — 154 customers (8.24%) ❓
5. **Competitor made better offer** — 140 customers (7.49%) 💰

**Critical Insight:** The #1 churn reason is support quality — an internal, controllable factor. This can be addressed without product changes or price reductions.

### ML Model Results
| Model | Accuracy | AUC Score | Best For |
|-------|----------|-----------|---------|
| **Logistic Regression** | **80.6%** | **0.847** | ✅ Winner — explainable |
| Random Forest | 79.6% | 0.831 | Good alternative |

**Top 3 Churn Predictors (Random Forest Feature Importance):**
1. Monthly Charges (0.173) — higher bills = higher churn risk
2. Tenure Months (0.172) — newer customers = higher churn risk
3. Total Charges (0.160) — closely correlated with tenure

---

## 📊 Python Visualizations

### 1. Customer Churn Distribution

![Churn Distribution](charts/churn_distribution.png)

**Key Insight:** 26.54% of 7,043 customers churned — 1,869 customers lost. At an average monthly charge of $74.44, this represents $139,130 in monthly recurring revenue at risk. Reducing churn by just 5 percentage points would recover approximately $26,000 per month.

---

### 2. Churn Rate by Contract Type

![Churn by Contract](charts/churn_by_contract.png)

**Key Insight:** Month-to-month contracts show catastrophic 42.7% churn rate versus 2.8% for two-year contracts. The business case for incentivizing longer contract commitments is overwhelming. A discount of even 15% on annual plans would be recovered within 2 months of reduced churn.

---

### 3. Churn Rate by Customer Tenure

![Churn by Tenure](charts/churn_by_tenure.png)

**Key Insight:** New customers (0-12 months) churn at 47.7% — nearly half leave within the first year. Churn drops dramatically with tenure, falling to 9.5% for customers who stay beyond 4 years. Investment in onboarding and first-year experience will have the highest retention ROI.

---

### 4. Monthly Charges Distribution by Churn Status

![Monthly Charges](charts/monthly_charges_churn.png)

**Key Insight:** Churned customers pay $74.44/month on average vs $61.27 for retained customers — a $13.17 gap. High-paying customers are churning at disproportionate rates, suggesting a value perception problem. These customers feel they are not getting value for premium pricing.

---

### 5. Top 8 Churn Reasons

![Top Churn Reasons](charts/top_churn_reasons.png)

**Key Insight:** Support attitude is the #1 driver of churn at 10.27% — an entirely internal and fixable issue. Three of the top 5 reasons are competitor-related (better speed, more data, better offers), indicating a product competitiveness gap. Addressing support quality alone could immediately reduce churn by 10%.

---

### 6. Model Comparison — Confusion Matrix

![Confusion Matrix](charts/confusion_matrix.png)

**Key Insight:** Logistic Regression correctly identifies 213 out of 374 churners in the test set (57% recall). For business deployment, improving recall is the priority — a false negative (missing a churner) costs more than a false positive (unnecessary retention offer).

---

### 7. Feature Importance — Random Forest

![Feature Importance](charts/feature_importance.png)

**Key Insight:** Monthly charges and tenure are nearly equal in predictive importance (0.173 vs 0.172), confirming that pricing and loyalty are the two primary churn levers. Contract type ranks 4th (0.080), validating the SQL finding that contract length is a critical retention tool.

---
## 🛠️ Technologies & Skills

### **Database & Querying**
- PostgreSQL 18
- pgAdmin 4
- Advanced SQL (CASE statements, CTEs, window functions, subqueries)

### **Data Exploration**
- Microsoft Excel (Pivot Tables, conditional formatting, data profiling)
- Initial EDA and quick insight generation

### **Programming & Analysis**
- Python 3.8+
- pandas (data manipulation & feature engineering)
- matplotlib + seaborn (statistical visualization)
- scikit-learn (machine learning, model evaluation)
- sqlalchemy + psycopg2 (database connectivity)
- openpyxl (Excel file handling)

### **Data Visualization & BI**
- Power BI Desktop (interactive dashboard)
- DAX (calculated columns and measures)
- Python visualization libraries (static charts)

### **SQL Techniques Demonstrated**
- ✅ Aggregate functions (SUM, COUNT, AVG, ROUND)
- ✅ GROUP BY, ORDER BY, LIMIT
- ✅ CASE statements (conditional segmentation)
- ✅ Window functions (OVER, SUM OVER)
- ✅ Subqueries and CTEs
- ✅ Type casting and precision control

### **Machine Learning Skills**
- ✅ Data preprocessing (Label Encoding, train/test split)
- ✅ Logistic Regression (baseline explainable model)
- ✅ Random Forest Classifier (ensemble method)
- ✅ Model evaluation (accuracy, AUC-ROC, confusion matrix)
- ✅ Feature importance analysis
- ✅ Classification report (precision, recall, F1-score)

### **Business Analysis**
- Customer churn analysis and segmentation
- Revenue at risk quantification
- Retention strategy development
- ROI calculation and prioritization
- Executive reporting and storytelling

---

## 📁 Repository Structure

```
customer-churn-prediction/
│
├── README.md                      # This file
├── churn_analysis.md              # Full analysis report (4,000+ words)
├── queries.sql                    # All 6 SQL queries with outputs
├── eda_analysis.py                # Python EDA visualization script
├── churn_model.py                 # ML model training and evaluation script
├── load_data.py                   # Data loading script (Excel → PostgreSQL)
│
├── charts/                        # All generated visualizations
│   ├── churn_distribution.png
│   ├── churn_by_contract.png
│   ├── churn_by_tenure.png
│   ├── monthly_charges_churn.png
│   ├── top_churn_reasons.png
│   ├── confusion_matrix.png
│   ├── feature_importance.png
│   └── powerbi_dashboard.png

```

---

## 🚀 How to Reproduce This Analysis

### Prerequisites
- PostgreSQL 18+ installed
- pgAdmin 4 (or any SQL client)
- Python 3.8+ with pip
- Microsoft Excel
- Power BI Desktop (free)

### Setup Steps

**1. Clone repository**
```bash
git clone https://github.com/[your-username]/customer-churn-prediction.git
cd customer-churn-prediction
```

**2. Install Python dependencies**
```bash
pip install pandas matplotlib seaborn scikit-learn sqlalchemy psycopg2-binary openpyxl
```

**3. Create PostgreSQL database**
```sql
CREATE DATABASE churn_analysis;
```

**4. Load data into PostgreSQL**
```bash
python load_data.py
```

**5. Run SQL analysis**
```bash
psql -d churn_analysis -f queries.sql
```

**6. Generate Python visualizations**
```bash
python eda_analysis.py
```

**7. Train ML model**
```bash
python churn_model.py
```

**8. Open Power BI Dashboard**
- Open `dashboard.pbix` in Power BI Desktop

---

## 📈 Results Summary

### Dataset Overview
- **Customers:** 7,043
- **Features:** 33 columns
- **Churn Rate:** 26.54%
- **Source:** IBM Telco Customer Churn Dataset
- **Geography:** California, USA

### Strategic Recommendations (ROI-Ranked)

**Priority 1: First-Year Onboarding Program**
- **Target:** 0-12 month customers (47.4% churn rate)
- **Investment:** $50/customer (dedicated onboarding + check-in calls)
- **Expected Churn Reduction:** 47.4% → 30%
- **Revenue Saved:** ~$380,000 annually
- **ROI:** 800%+
- **Timeline:** 30 days to implement

**Priority 2: Contract Upgrade Incentive**
- **Target:** 3,875 month-to-month customers
- **Offer:** 15% discount for switching to annual plan
- **Expected Conversion:** 10% (387 customers)
- **Revenue Protected:** ~$346,000 annually
- **ROI:** 500%+
- **Timeline:** 60 days

**Priority 3: Support Quality Initiative**
- **Target:** Fix #1 churn reason (support attitude — 192 customers)
- **Investment:** Support training program
- **Expected Churn Reduction:** 10% of current churners
- **Revenue Saved:** ~$170,000 annually
- **ROI:** 300%+
- **Timeline:** 90 days

**Priority 4: Fiber Optic Retention Campaign**
- **Target:** 3,096 fiber optic customers (41.9% churn)
- **Offer:** Service upgrade + speed guarantee
- **Expected Churn Reduction:** 41.9% → 30%
- **Revenue Protected:** ~$200,000 annually
- **ROI:** 400%+
- **Timeline:** 45 days

### Projected Total Impact
**Revenue Recovered:** $1,096,000+ annually
**Churn Rate Reduction:** 26.54% → ~18% (target)
**Customer Lifetime Value:** +35% improvement

---

## 🎓 Skills Demonstrated

**Technical Skills:**
- ✅ **SQL Mastery:** 6 complex business queries on 7,043 row dataset with window functions and CTEs
- ✅ **Python EDA:** 5 professional statistical charts with business insight annotations
- ✅ **Machine Learning:** Two model comparison with evaluation metrics and feature importance
- ✅ **Power BI:** 6-visual interactive dashboard with DAX calculated columns and slicers
- ✅ **Excel:** Pivot table analysis and data profiling as first-pass exploration
- ✅ **Data Pipeline:** End-to-end from raw Excel → PostgreSQL → Python → Power BI

**Analytical Skills:**
- ✅ **Business Acumen:** Translated model outputs into dollar-value revenue impact
- ✅ **Risk Quantification:** $1.67M annual revenue at risk calculation
- ✅ **Segmentation:** Contract type, tenure, payment method, and value-based customer segments
- ✅ **Strategic Thinking:** ROI-ranked recommendations with timelines and investment estimates

**Communication Skills:**
- ✅ **Data Storytelling:** Each chart paired with a business insight, not just a description
- ✅ **Executive Reporting:** 4,000+ word analysis report written for non-technical stakeholders
- ✅ **Dashboard Design:** Color-coded visuals (traffic light system) for instant comprehension

---

## 🤝 Connect With Me

I'm actively seeking **Data Analyst** opportunities where I can apply SQL, Python, machine learning, and Power BI skills to solve real business problems through data.

**Open to:**
- Full-time Data Analyst positions
- Business Intelligence / BI Analyst roles
- Internships in Data Analytics or Data Science
- Freelance analytics projects

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
Feel free to use this code for learning purposes. If you use this project in your portfolio, please provide attribution.

---

## 🙏 Acknowledgments

- Dataset: [IBM Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) via Kaggle
- Analysis framework inspired by industry churn management best practices
- ML approach based on scikit-learn documentation and examples
- Dashboard design principles from Microsoft Power BI community

---

## ⭐ Show Your Support

If you found this analysis helpful or learned something from the code:

- **Star this repository** ⭐
- **Fork it** to build your own version 🍴
- **Share it** with others learning data analytics 📢
- **Connect with me** on LinkedIn 🤝

**Thank you for visiting!** 🙏
