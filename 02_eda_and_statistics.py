# -*- coding: utf-8 -*-
"""
Module 02: Exploratory Data Analysis & 5 Analytical Questions
"""
import pandas as pd

df = pd.read_csv("ecommerce_customer_churn.csv").drop_duplicates()
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())
df["OrderCount"] = df["OrderCount"].fillna(df["OrderCount"].median())
df["CashbackAmount"] = df["CashbackAmount"].fillna(df["CashbackAmount"].mean())
df["SatisfactionScore"] = df["SatisfactionScore"].fillna(df["SatisfactionScore"].mode()[0])

print("--- Q1: Overall Proportion ---")
print((df['Churn'].value_counts(normalize=True)*100).round(1))

print("\n--- Q2: Churn by Payment Mode ---")
print((df.groupby('PreferredPaymentMode')['Churn'].mean()*100).sort_values(ascending=False).round(1))

print("\n--- Q3: Churn by Satisfaction Score ---")
print((df.groupby('SatisfactionScore')['Churn'].mean()*100).round(1))

print("\n--- Q4: Tenure by Churn Status ---")
print(df.groupby('Churn')['Tenure'].agg(['mean', 'median']).round(1))

print("\n--- Q5: Correlation with OrderCount ---")
print("Correlation:", round(df['OrderCount'].corr(df['Churn']), 4))
