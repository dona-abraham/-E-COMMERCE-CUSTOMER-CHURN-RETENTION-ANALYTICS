# E-Commerce Customer Churn & Retention Analytics

**Author:** Dona Abraham  
**Domain:** E-Commerce / Retail Analytics  
**Tools & Technologies:** Python (Spyder 6, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn), Power BI, Tableau, Microsoft Excel  

---

## 📌 Executive Summary
Customer attrition presents a substantial financial risk to e-commerce enterprises, where customer acquisition expenses consistently outpace retention costs. This project conducts an end-to-end analytical investigation into customer churn patterns across an e-commerce platform dataset of **1,500 validated customer records** and **11 behavioral and demographic dimensions**.

Using descriptive statistics, exploratory data analysis (EDA), predictive modeling via **Logistic Regression (89.33% accuracy)**, and interactive dashboards in **Power BI** and **Tableau**, this repository surfaces actionable, data-driven retention strategies.

---

## 📊 Key Findings & EDA Insights

| Analytical Dimension | Observation / Metric | Retention Takeaway |
| :--- | :--- | :--- |
| **Overall Retention vs. Churn** | Retained: **62.0% (930)** \| Churned: **38.0% (570)** | Platform baseline churn requires targeted proactive intervention. |
| **Preferred Payment Mode** | **Cash on Delivery (COD)** has highest churn (**58.6%**), followed by E-Wallet (**47.8%**). Debit Card (**33.6%**) has lowest. | COD customers lack financial stickiness; incentivize prepaid and digital wallet lock-in. |
| **Customer Satisfaction** | Rating 1 Star: **70.7% churn** vs. Rating 5 Stars: **8.8% churn**. | Low satisfaction is an acute churn trigger; automate support outreach for ratings $\le 2$. |
| **Customer Tenure** | Retained mean: **17.1 months** vs. Churned mean: **5.4 months**. | Critical attrition vulnerability window occurs within the first **0 to 6 months** of onboarding. |
| **Order Frequency** | Pearson correlation with churn: **$r = -0.4125$**. | Infrequent purchasers churn at drastically higher rates; deploy loyalty milestone perks. |

---

## 🤖 Machine Learning Model: Logistic Regression

A binary Logistic Regression classifier was trained on an 80/20 train-test split (StandardScaler normalized features):

* **Overall Test Accuracy:** `89.33%`
* **Retained (Class 0):** Precision = `0.8939` | Recall = `0.9399` | F1-Score = `0.9163`
* **Churned (Class 1):** Precision = `0.8923` | Recall = `0.8169` | F1-Score = `0.8529`
* **Confusion Matrix:**
  * True Negatives (Retained Correct): `219`
  * False Positives (Retained Misclassified Churn): `14`
  * False Negatives (Churned Misclassified Retain): `26`
  * True Positives (Churned Correct): `116`

---

## 📈 Visualizations Generated

The analysis pipeline generates 6 publication-grade figures saved directly to this repository:
1. `01_customer_status_pie.png` — Customer Retention vs. Churn Distribution (Donut Chart)
2. `02_payment_mode_bar.png` — Churn Rate Across Preferred Payment Modes
3. `03_satisfaction_bar.png` — Churn Rate by Customer Satisfaction Rating (1–5 Stars)
4. `04_tenure_bar.png` — Mean Customer Tenure by Churn Status
5. `05_correlation_heatmap.png` — Correlation Matrix of Quantitative Attributes
6. `06_tenure_ordercount_scatter.png` — Customer Tenure vs. Order Count Relationship

---

## 📁 Repository Structure

```text
Customer_Churn_And_Retension_Analysis/
├── ecommerce_customer_churn.csv       # Primary cleaned dataset (1,500 records)
├── ecommerce_customer_churn.xlsx      # Microsoft Excel formatted dataset
├── main_analysis.py                   # Complete unified end-to-end Python script
├── 01_data_preprocessing.py           # Preprocessing & imputation module
├── 02_eda_and_statistics.py           # Descriptive statistics & analytical questions
├── 03_logistic_regression.py          # Machine learning model training & evaluation
├── 04_visualizations.py               # Matplotlib & Seaborn visualization pipeline
├── 05_generate_tableau_dashboard.py   # Tableau extract & dashboard generator
├── 01_customer_status_pie.png         # Figure 1: Donut chart
├── 02_payment_mode_bar.png            # Figure 2: Payment mode churn bar chart
├── 03_satisfaction_bar.png            # Figure 3: Satisfaction score churn bar chart
├── 04_tenure_bar.png                  # Figure 4: Tenure bar chart
├── 05_correlation_heatmap.png         # Figure 5: Correlation heatmap
├── 06_tenure_ordercount_scatter.png   # Figure 6: Scatter plot (Tenure vs OrderCount)
└── README.md                          # Project documentation
```

---

## 🚀 Execution Guide (Spyder 6 / Python)

### Prerequisites
Install required Python libraries:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl
```

### Running in Spyder 6
1. Open **Spyder 6**.
2. Select **File &rarr; Open** and open `main_analysis.py`.
3. Press **F5** (or click the green **Run** button).
4. The terminal will display complete descriptive statistics, question summaries, model performance metrics, and save all 6 visualization plots in the project directory.
