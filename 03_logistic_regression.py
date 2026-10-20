# -*- coding: utf-8 -*-
"""
Module 03: Machine Learning Classification (Logistic Regression)
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_csv("ecommerce_customer_churn.csv").drop_duplicates()
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].median())
df["OrderCount"] = df["OrderCount"].fillna(df["OrderCount"].median())
df["CashbackAmount"] = df["CashbackAmount"].fillna(df["CashbackAmount"].mean())
df["SatisfactionScore"] = df["SatisfactionScore"].fillna(df["SatisfactionScore"].mode()[0])

categorical_cols = ['Gender', 'CityTier', 'Membership', 'PreferredPaymentMode']
df_encoded = pd.get_dummies(df.drop(columns=['CustomerID']), columns=categorical_cols, drop_first=True)

X = df_encoded.drop(columns=['Churn'])
y = df_encoded['Churn']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_reg = LogisticRegression(max_iter=1000, random_state=42)
log_reg.fit(X_train_scaled, y_train)

y_pred = log_reg.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred, digits=4))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
