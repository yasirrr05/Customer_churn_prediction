import pandas as pd
from sqlalchemy import create_engine

# Load Excel file
df = pd.read_excel(r'YOUR_EXCEL_SHEET_FILE_PATH', 
                   sheet_name='YOUR_SHEET_NAME')

# Clean column names (lowercase, replace spaces with underscores)
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Check data loaded correctly
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(df.head(2))

# Connect to PostgreSQL and load data
engine = create_engine('postgresql://postgres:"YOUR_POSTGRESQL_PASSWORD"@localhost:5432/churn_analysis')
df.to_sql('telco_churn', engine, if_exists='replace', index=False)

print("✅ Data loaded successfully!")