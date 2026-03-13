import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, classification_report,
                             confusion_matrix, roc_auc_score)
import os

# ── Settings ──────────────────────────────────────────
sns.set_theme(style='whitegrid')
plt.rcParams['figure.dpi'] = 150
os.makedirs('charts', exist_ok=True)

# ── Load Data ──────────────────────────────────────────
df = pd.read_excel(r'C:\Users\khali\Desktop\Customer_Churn_Prediction\Telco_customer_churn.xlsx',
                   sheet_name='Telco_Churn')
df.columns = df.columns.str.lower().str.replace(' ', '_')
print(f"✅ Data loaded: {df.shape}")

# ── Data Preprocessing ─────────────────────────────────
# Select relevant features only
features = [
    'tenure_months', 'monthly_charges', 'total_charges',
    'gender', 'senior_citizen', 'partner', 'dependents',
    'phone_service', 'multiple_lines', 'internet_service',
    'online_security', 'online_backup', 'device_protection',
    'tech_support', 'streaming_tv', 'streaming_movies',
    'contract', 'paperless_billing', 'payment_method'
]

df_model = df[features + ['churn_label']].copy()

# Drop rows with missing values
df_model = df_model.dropna()
print(f"✅ After cleaning: {df_model.shape}")

# Encode categorical columns
le = LabelEncoder()
categorical_cols = df_model.select_dtypes(include='object').columns.tolist()
categorical_cols.remove('churn_label')

for col in categorical_cols:
    df_model[col] = le.fit_transform(df_model[col].astype(str))

# Encode target variable
df_model['churn_label'] = (df_model['churn_label'] == 'Yes').astype(int)

print(f"✅ Encoding complete")
print(f"   Churn rate in dataset: {df_model['churn_label'].mean()*100:.1f}%")

# ── Split Data ─────────────────────────────────────────
X = df_model[features]
y = df_model['churn_label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

print(f"\n✅ Data split:")
print(f"   Training set: {X_train.shape[0]} rows")
print(f"   Testing set:  {X_test.shape[0]} rows")

# ── Model 1: Logistic Regression ───────────────────────
print("\n--- Logistic Regression ---")
lr_model = LogisticRegression(max_iter=3000, random_state=42)
lr_model.fit(X_train, y_train)
lr_pred = lr_model.predict(X_test)
lr_accuracy = accuracy_score(y_test, lr_pred)
lr_auc = roc_auc_score(y_test, lr_model.predict_proba(X_test)[:,1])
print(f"Accuracy: {lr_accuracy*100:.1f}%")
print(f"AUC Score: {lr_auc:.3f}")
print(classification_report(y_test, lr_pred, target_names=['Retained', 'Churned']))

# ── Model 2: Random Forest ─────────────────────────────
print("\n--- Random Forest ---")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_accuracy = accuracy_score(y_test, rf_pred)
rf_auc = roc_auc_score(y_test, rf_model.predict_proba(X_test)[:,1])
print(f"Accuracy: {rf_accuracy*100:.1f}%")
print(f"AUC Score: {rf_auc:.3f}")
print(classification_report(y_test, rf_pred, target_names=['Retained', 'Churned']))

# ── Chart 6: Confusion Matrix ──────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, pred, title in zip(axes,
                            [lr_pred, rf_pred],
                            ['Logistic Regression', 'Random Forest']):
    cm = confusion_matrix(y_test, pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Retained', 'Churned'],
                yticklabels=['Retained', 'Churned'])
    ax.set_title(f'{title}\nAccuracy: {accuracy_score(y_test, pred)*100:.1f}%',
                 fontsize=13, fontweight='bold')
    ax.set_ylabel('Actual', fontsize=11)
    ax.set_xlabel('Predicted', fontsize=11)

plt.suptitle('Model Comparison - Confusion Matrix',
             fontsize=15, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('charts/confusion_matrix.png', bbox_inches='tight')
plt.show()
print("✅ Chart 6 saved")

# ── Chart 7: Feature Importance ───────────────────────
feature_importance = pd.DataFrame({
    'feature': features,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=True).tail(10)

fig, ax = plt.subplots(figsize=(10, 6))
colors = sns.color_palette('RdYlGn', len(feature_importance))
bars = ax.barh(feature_importance['feature'],
               feature_importance['importance'],
               color=colors, edgecolor='white')

for bar, val in zip(bars, feature_importance['importance']):
    ax.text(bar.get_width() + 0.002, bar.get_y() + bar.get_height()/2,
            f'{val:.3f}', va='center', fontsize=10, fontweight='bold')

ax.set_title('Top 10 Features Predicting Customer Churn\n(Random Forest)',
             fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Feature Importance Score', fontsize=11)
ax.set_xlim(0, feature_importance['importance'].max() + 0.05)
plt.tight_layout()
plt.savefig('charts/feature_importance.png', bbox_inches='tight')
plt.show()
print("✅ Chart 7 saved")

# ── Model Comparison Summary ───────────────────────────
print("\n" + "="*50)
print("MODEL COMPARISON SUMMARY")
print("="*50)
print(f"{'Model':<25} {'Accuracy':>10} {'AUC Score':>10}")
print("-"*50)
print(f"{'Logistic Regression':<25} {lr_accuracy*100:>9.1f}% {lr_auc:>10.3f}")
print(f"{'Random Forest':<25} {rf_accuracy*100:>9.1f}% {rf_auc:>10.3f}")
print("="*50)
print(f"\n🏆 Best Model: {'Random Forest' if rf_accuracy > lr_accuracy else 'Logistic Regression'}")
print(f"\n🎉 All charts saved to charts/ folder!")