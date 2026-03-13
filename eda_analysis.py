import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── Settings ──────────────────────────────────────────
sns.set_theme(style='whitegrid')
plt.rcParams['figure.dpi'] = 150

# Create charts folder
os.makedirs('charts', exist_ok=True)

# ── Load Data ──────────────────────────────────────────
df = pd.read_excel(r'C:\Users\khali\Desktop\Customer_Churn_Prediction\Telco_customer_churn.xlsx',
                   sheet_name='Telco_Churn')
df.columns = df.columns.str.lower().str.replace(' ', '_')

print(f"Dataset Shape: {df.shape}")
print(f"\nColumn Names:\n{df.columns.tolist()}")
print(f"\nMissing Values:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
print(f"\nChurn Distribution:\n{df['churn_label'].value_counts()}")

# ── Chart 1 — Churn Distribution ──────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
colors = ['#2ecc71', '#e74c3c']
counts = df['churn_label'].value_counts()
bars = ax.bar(counts.index, counts.values, color=colors, width=0.4, edgecolor='white')

for bar, count in zip(bars, counts.values):
    pct = count / len(df) * 100
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
            f'{count}\n({pct:.1f}%)', ha='center', fontsize=12, fontweight='bold')

ax.set_title('Customer Churn Distribution', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Churn Status', fontsize=12)
ax.set_ylabel('Number of Customers', fontsize=12)
ax.set_ylim(0, 6500)
plt.tight_layout()
plt.savefig('charts/churn_distribution.png')
plt.show()
print("✅ Chart 1 saved")

# ── Chart 2 — Churn by Contract Type ──────────────────
contract_churn = df.groupby('contract')['churn_label'].apply(
    lambda x: (x == 'Yes').sum() / len(x) * 100).reset_index()
contract_churn.columns = ['contract', 'churn_rate']
contract_churn = contract_churn.sort_values('churn_rate', ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
colors = ['#e74c3c', '#f39c12', '#2ecc71']
bars = ax.bar(contract_churn['contract'], contract_churn['churn_rate'],
              color=colors, width=0.4, edgecolor='white')

for bar, rate in zip(bars, contract_churn['churn_rate']):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{rate:.1f}%', ha='center', fontsize=12, fontweight='bold')

ax.set_title('Churn Rate by Contract Type', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Contract Type', fontsize=12)
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_ylim(0, 55)
plt.tight_layout()
plt.savefig('charts/churn_by_contract.png')
plt.show()
print("✅ Chart 2 saved")

# ── Chart 3 — Churn by Tenure Group ───────────────────
df['tenure_group'] = pd.cut(df['tenure_months'],
                             bins=[0, 12, 24, 48, 100],
                             labels=['0-12 Months', '13-24 Months',
                                     '25-48 Months', '49+ Months'])

tenure_churn = df.groupby('tenure_group', observed=True)['churn_label'].apply(
    lambda x: (x == 'Yes').sum() / len(x) * 100).reset_index()
tenure_churn.columns = ['tenure_group', 'churn_rate']

fig, ax = plt.subplots(figsize=(9, 5))
colors = ['#e74c3c', '#e67e22', '#f1c40f', '#2ecc71']
bars = ax.bar(tenure_churn['tenure_group'], tenure_churn['churn_rate'],
              color=colors, width=0.4, edgecolor='white')

for bar, rate in zip(bars, tenure_churn['churn_rate']):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
            f'{rate:.1f}%', ha='center', fontsize=12, fontweight='bold')

ax.set_title('Churn Rate by Customer Tenure', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Tenure Group', fontsize=12)
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_ylim(0, 60)
plt.tight_layout()
plt.savefig('charts/churn_by_tenure.png')
plt.show()
print("✅ Chart 3 saved")

# ── Chart 4 — Monthly Charges vs Churn ────────────────
fig, ax = plt.subplots(figsize=(9, 5))
churned = df[df['churn_label'] == 'Yes']['monthly_charges']
retained = df[df['churn_label'] == 'No']['monthly_charges']

ax.hist(retained, bins=30, alpha=0.6, color='#2ecc71', label='Retained (No Churn)')
ax.hist(churned, bins=30, alpha=0.6, color='#e74c3c', label='Churned')

ax.axvline(churned.mean(), color='#c0392b', linestyle='--', linewidth=2,
           label=f'Churned Avg: ${churned.mean():.2f}')
ax.axvline(retained.mean(), color='#27ae60', linestyle='--', linewidth=2,
           label=f'Retained Avg: ${retained.mean():.2f}')

ax.set_title('Monthly Charges Distribution by Churn Status',
             fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Monthly Charges ($)', fontsize=12)
ax.set_ylabel('Number of Customers', fontsize=12)
ax.legend(fontsize=10)
plt.tight_layout()
plt.savefig('charts/monthly_charges_churn.png')
plt.show()
print("✅ Chart 4 saved")

# ── Chart 5 — Top Churn Reasons ───────────────────────
top_reasons = df[df['churn_label'] == 'Yes']['churn_reason'].value_counts().head(8)

fig, ax = plt.subplots(figsize=(11, 6))
colors = sns.color_palette('Reds_r', len(top_reasons))
bars = ax.barh(top_reasons.index, top_reasons.values, color=colors, edgecolor='white')

for bar, count in zip(bars, top_reasons.values):
    ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
            str(count), va='center', fontsize=11, fontweight='bold')

ax.set_title('Top 8 Reasons Customers Churn', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Number of Customers', fontsize=12)
ax.set_xlim(0, top_reasons.max() + 30)
plt.tight_layout()
plt.savefig('charts/top_churn_reasons.png')
plt.show()
print("✅ Chart 5 saved")

print("\n🎉 All 5 charts saved to charts/ folder!")
print(f"\nKey Insights:")
print(f"  Overall Churn Rate: {(df['churn_label'] == 'Yes').mean()*100:.1f}%")
print(f"  Avg Monthly Charge (Churned): ${df[df['churn_label']=='Yes']['monthly_charges'].mean():.2f}")
print(f"  Avg Monthly Charge (Retained): ${df[df['churn_label']=='No']['monthly_charges'].mean():.2f}")