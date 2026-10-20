# -*- coding: utf-8 -*-
"""
==============================================================================
PROJECT: E-COMMERCE CUSTOMER CHURN & RETENTION ANALYTICS
AUTHOR : Dona Abraham (Roll No: 2501722037003)
IDE    : Spyder 6 / Python 3.11+
==============================================================================
This master script performs complete end-to-end customer churn analytics:
  1. Data Loading & Inspection
  2. Data Preprocessing & Missing-Value Imputation
  3. Exploratory Data Analysis & 5 Analytical Research Questions
  4. Machine Learning Classification (Logistic Regression)
  5. Statistical & Analytical Visualizations (Figures 1 to 6)
  6. Comprehensive Business Summary Report
==============================================================================
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Configure publication aesthetics for Spyder 6
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.autolayout'] = True

# ------------------------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------------------------
file_path = "ecommerce_customer_churn.csv"
if not os.path.exists(file_path):
    file_path = os.path.join(r"C:\Users\Lenovo\OneDrive\Desktop\DAV", "ecommerce_customer_churn.csv")

df_raw = pd.read_csv(file_path)
print("==============================================================")
print("1. DATASET LOADED SUCCESSFULLY")
print("==============================================================")
print(f"Initial Shape: {df_raw.shape[0]:,} Rows x {df_raw.shape[1]} Columns")
print("\nFirst 5 Sample Records:")
print(df_raw.head())

# ------------------------------------------------------------------------------
# 2. DATA PREPROCESSING & CLEANING
# ------------------------------------------------------------------------------
print("\n==============================================================")
print("2. DATA PREPROCESSING & CLEANING")
print("==============================================================")

# Duplicate Removal
initial_count = len(df_raw)
df = df_raw.drop_duplicates().copy()
print(f"Duplicate Records Removed : {initial_count - len(df):,}")
print(f"Cleaned Dataset Shape     : {df.shape[0]:,} Rows x {df.shape[1]} Columns")

# Missing Values Imputation
# Impute continuous variables with Median (robust to skewness)
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())
df["OrderCount"] = df["OrderCount"].fillna(df["OrderCount"].median())

# Impute CashbackAmount with Mean
df["CashbackAmount"] = df["CashbackAmount"].fillna(df["CashbackAmount"].mean())

# Impute SatisfactionScore with Mode
df["SatisfactionScore"] = df["SatisfactionScore"].fillna(df["SatisfactionScore"].mode()[0])

print("\nMissing Values After Imputation:")
print(df.isnull().sum())

# ------------------------------------------------------------------------------
# 3. EXPLORATORY DATA ANALYSIS (EDA) & 5 ANALYTICAL QUESTIONS
# ------------------------------------------------------------------------------
print("\n==============================================================")
print("3. DESCRIPTIVE STATISTICS & ANALYTICAL QUESTIONS")
print("==============================================================")
numeric_cols = ["Age", "Tenure", "OrderCount", "CashbackAmount", "SatisfactionScore", "Churn"]
print("\nDescriptive Statistics Summary:")
print(df[numeric_cols].describe().round(2))

# Q1. Overall proportion of churned versus retained customers
print("\n--- Q1: Overall Customer Churn vs. Retention ---")
churn_dist = df["Churn"].value_counts(normalize=True) * 100
counts = df["Churn"].value_counts()
print(f"  Retained (0) : {counts.get(0, 0):,} ({churn_dist.get(0, 0.0):.1f}%)")
print(f"  Churned  (1) : {counts.get(1, 0):,} ({churn_dist.get(1, 0.0):.1f}%)")

# Q2. Churn rate across preferred payment modes
print("\n--- Q2: Churn Rate by Preferred Payment Mode ---")
pay_churn = df.groupby("PreferredPaymentMode")["Churn"].mean().mul(100).sort_values(ascending=False)
for mode, rate in pay_churn.items():
    print(f"  {mode:20}: {rate:.1f}%")

# Q3. Churn rate across customer satisfaction scores
print("\n--- Q3: Churn Rate by Customer Satisfaction Rating ---")
csat_churn = df.groupby("SatisfactionScore")["Churn"].mean().mul(100).sort_index()
for score, rate in csat_churn.items():
    print(f"  Rating {score:.0f} Star(s)        : {rate:.1f}%")

# Q4. Influence of customer tenure on retention
print("\n--- Q4: Tenure by Customer Status ---")
tenure_stats = df.groupby("Churn")["Tenure"].agg(["mean", "median"]).round(1)
print(f"  Retained (0) Mean Tenure : {tenure_stats.loc[0, 'mean']} months (Median: {tenure_stats.loc[0, 'median']} mo)")
print(f"  Churned  (1) Mean Tenure : {tenure_stats.loc[1, 'mean']} months (Median: {tenure_stats.loc[1, 'median']} mo)")

# Q5. Relationship between order count and churn
corr_val = df["OrderCount"].corr(df["Churn"])
print("\n--- Q5: Correlation Between Order Count and Churn ---")
print(f"  Pearson Correlation: {corr_val:.4f} (Substantial Negative Association)")

# ------------------------------------------------------------------------------
# 4. SUPERVISED MACHINE LEARNING (LOGISTIC REGRESSION)
# ------------------------------------------------------------------------------
print("\n==============================================================")
print("4. MACHINE LEARNING MODEL - LOGISTIC REGRESSION")
print("==============================================================")
categorical_cols = ["Gender", "CityTier", "Membership", "PreferredPaymentMode"]
X_encoded = pd.get_dummies(df.drop(columns=["CustomerID", "Churn"]), columns=categorical_cols, drop_first=True)
y = df["Churn"]

# Stratified 75% train / 25% test split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.25, random_state=42, stratify=y
)

# Standardize numerical features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression model
log_reg = LogisticRegression(max_iter=1000, random_state=42)
log_reg.fit(X_train_scaled, y_train)

# Predictions and Evaluation
y_pred = log_reg.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred) * 100

print(f"Overall Model Accuracy : {acc:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Retained (0)", "Churned (1)"], digits=4))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(f"  True Negatives  (Retained Correctly Predicted) : {cm[0, 0]:,}")
print(f"  False Positives (Retained Misclassified Churn) : {cm[0, 1]:,}")
print(f"  False Negatives (Churned Misclassified Retain) : {cm[1, 0]:,}")
print(f"  True Positives  (Churned Correctly Predicted)  : {cm[1, 1]:,}")

# ------------------------------------------------------------------------------
# 5. PUBLICATION-QUALITY FIGURES GENERATION (FIGURES 1 TO 6)
# ------------------------------------------------------------------------------
print("\n==============================================================")
print("5. GENERATING PUBLICATION-QUALITY FIGURES")
print("==============================================================")

# Figure 1: Pie Chart - Customer Retention and Churn
plt.figure(figsize=(7, 5))
status_counts = df["Churn"].map({0: "Retained", 1: "Churned"}).value_counts()
status_counts = status_counts.reindex(["Retained", "Churned"])
plt.pie(status_counts.values, labels=[f"{k} ({v/len(df)*100:.1f}%)" for k, v in status_counts.items()],
        autopct="%1.1f%%", startangle=90)
plt.title("Overall Customer Retention and Churn")
plt.tight_layout()
plt.savefig("01_customer_status_pie.png", dpi=300)
print("  [Saved] 01_customer_status_pie.png")
plt.close()

# Figure 2: Bar Chart - Churn Rate by Preferred Payment Mode
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
print("  [Saved] 02_payment_mode_bar.png")
plt.close()

# Figure 3: Bar Chart - Churn Rate by Satisfaction Score
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
print("  [Saved] 03_satisfaction_bar.png")
plt.close()

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
print("  [Saved] 04_tenure_bar.png")
plt.close()

# Figure 5: Correlation Heatmap
corr_df = df[numeric_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_df, annot=True, fmt=".2f", cmap="coolwarm", center=0, linewidths=0.5)
plt.title("Correlation Heatmap of Customer Analytics Variables")
plt.tight_layout()
plt.savefig("05_correlation_heatmap.png", dpi=300)
print("  [Saved] 05_correlation_heatmap.png")
plt.close()

# Figure 6: Scatter Plot - Tenure vs. Order Count (Exact Document Alignment)
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
print("  [Saved] 06_tenure_ordercount_scatter.png")
plt.close()

# ------------------------------------------------------------------------------
# 6. EXECUTIVE SUMMARY CONSOLE REPORT
# ------------------------------------------------------------------------------
total_cust = len(df)
churn_cust = int(df["Churn"].sum())
retain_cust = total_cust - churn_cust

print("\n==============================================================")
print("E-COMMERCE CUSTOMER CHURN ANALYTICS - FINAL SUMMARY")
print("==============================================================")
print(f"Total Customers Analyzed : {total_cust:,}")
print(f"Retained Customers       : {retain_cust:,} ({(retain_cust/total_cust)*100:.1f}%)")
print(f"Churned Customers        : {churn_cust:,} ({(churn_cust/total_cust)*100:.1f}%)")
print(f"Average Customer Tenure  : {df['Tenure'].mean():.2f} Months")
print(f"Average Order Count      : {df['OrderCount'].mean():.2f} Orders")
print(f"Average Cashback Amount  : ${df['CashbackAmount'].mean():.2f}")
print(f"Average Satisfaction     : {df['SatisfactionScore'].mean():.2f} / 5.0 Stars")
print(f"Logistic Regression Acc  : {acc:.2f}%")
print("==============================================================")
