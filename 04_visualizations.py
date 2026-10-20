# -*- coding: utf-8 -*-
"""
Module 04: Visualizations (Figures 1 to 6)
Author: Dona Abraham (Roll No: 2501722037003)
Environment: Spyder 6 / Python 3.11+
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("ecommerce_customer_churn.csv").drop_duplicates()
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())
df["OrderCount"] = df["OrderCount"].fillna(df["OrderCount"].median())
df["CashbackAmount"] = df["CashbackAmount"].fillna(df["CashbackAmount"].mean())
df["SatisfactionScore"] = df["SatisfactionScore"].fillna(df["SatisfactionScore"].mode()[0])

plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.autolayout'] = True

# Figure 1: Pie Chart - Customer Retention and Churn
status_counts = df["Churn"].map({0: "Retained", 1: "Churned"}).value_counts()
status_counts = status_counts.reindex(["Retained", "Churned"])
plt.figure(figsize=(7, 5))
plt.pie(status_counts.values, labels=[f"{k} ({v/len(df)*100:.1f}%)" for k, v in status_counts.items()],
        autopct="%1.1f%%", startangle=90)
plt.title("Overall Customer Retention and Churn")
plt.tight_layout()
plt.savefig("01_customer_status_pie.png", dpi=300)
plt.show()

# Figure 2: Bar Chart - Churn Rate by Preferred Payment Mode
pay_churn = df.groupby("PreferredPaymentMode")["Churn"].mean().mul(100).sort_values(ascending=False)
plt.figure(figsize=(8, 5))
bars = plt.bar(pay_churn.index, pay_churn.values)
plt.title("Churn Rate by Preferred Payment Mode")
plt.xlabel("Preferred Payment Mode")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 60)
plt.xticks(rotation=20)
plt.grid(axis="y", alpha=0.25)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha="center")
plt.tight_layout()
plt.savefig("02_payment_mode_bar.png", dpi=300)
plt.show()

# Figure 3: Bar Chart - Churn Rate by Satisfaction Score
csat_churn = df.groupby("SatisfactionScore")["Churn"].mean().mul(100).sort_index()
plt.figure(figsize=(8, 5))
bars = plt.bar(csat_churn.index.astype(str), csat_churn.values)
plt.title("Churn Rate by Customer Satisfaction Score")
plt.xlabel("Satisfaction Score (Stars)")
plt.ylabel("Churn Rate (%)")
plt.ylim(0, 80)
plt.grid(axis="y", alpha=0.25)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, f"{yval:.1f}%", ha="center")
plt.tight_layout()
plt.savefig("03_satisfaction_bar.png", dpi=300)
plt.show()

# Figure 4: Bar Chart - Average Tenure by Churn Status
df["CustomerStatus"] = df["Churn"].map({0: "Retained", 1: "Churned"})
tenure_mean = df.groupby("CustomerStatus")["Tenure"].mean().reindex(["Retained", "Churned"])
plt.figure(figsize=(7, 5))
bars = plt.bar(tenure_mean.index, tenure_mean.values)
plt.title("Average Customer Tenure by Churn Status")
plt.xlabel("Customer Status")
plt.ylabel("Average Tenure (Months)")
plt.ylim(0, 21)
plt.grid(axis="y", alpha=0.25)
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.4, f"{yval:.1f}", ha="center")
plt.tight_layout()
plt.savefig("04_tenure_bar.png", dpi=300)
plt.show()

# Figure 5: Correlation Heatmap
numeric_cols = ["Age", "Tenure", "OrderCount", "CashbackAmount", "SatisfactionScore", "Churn"]
corr_df = df[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="coolwarm", center=0, linewidths=0.5)
plt.title("Correlation Heatmap of Customer Analytics Variables")
plt.tight_layout()
plt.savefig("05_correlation_heatmap.png", dpi=300)
plt.show()

# Figure 6: Scatter Plot - Tenure vs. Order Count (Exact Figure Alignment)
plt.figure(figsize=(8, 5))
plt.scatter(df["Tenure"], df["OrderCount"], alpha=0.25, s=12, color="tab:blue", edgecolors="none")
plt.title("Tenure vs. Order Count")
plt.xlabel("Tenure (Months)")
plt.ylabel("Order Count")
plt.xlim(0, 60)
plt.ylim(0, 26)
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig("06_tenure_ordercount_scatter.png", dpi=300)
plt.show()
