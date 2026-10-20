# -*- coding: utf-8 -*-
"""
Module 01: Data Loading & Preprocessing
"""
import pandas as pd

df = pd.read_csv("ecommerce_customer_churn.csv")
print("Initial Dataset Shape:", df.shape)

# Drop duplicate records
df = df.drop_duplicates().copy()
print("Shape After Removing Duplicates:", df.shape)

# Impute missing values
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())
df["OrderCount"] = df["OrderCount"].fillna(df["OrderCount"].median())
df["CashbackAmount"] = df["CashbackAmount"].fillna(df["CashbackAmount"].mean())
df["SatisfactionScore"] = df["SatisfactionScore"].fillna(df["SatisfactionScore"].mode()[0])

print("\nMissing Values After Imputation:")
print(df.isnull().sum())

# One-hot encoding
categorical_cols = ['Gender', 'CityTier', 'Membership', 'PreferredPaymentMode']
df_encoded = pd.get_dummies(df.drop(columns=['CustomerID']), columns=categorical_cols, drop_first=True)
print("\nEncoded Feature Set Shape:", df_encoded.shape)
