import pandas as pd
coffee = pd.read_csv(r"complete-pandas-tutorial\warmup-data\coffee.csv")
results = pd.read_parquet(r"complete-pandas-tutorial\data\results.parquet")
olympics_data = pd.read_excel(r"complete-pandas-tutorial\data\olympics-data.xlsx", sheet_name="results")

print(coffee.head())
print(results.head())
print(olympics_data.head())