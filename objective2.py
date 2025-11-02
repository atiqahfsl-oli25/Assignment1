import pandas as pd


def preprocess_data(df: pd.DataFrame):
df = df.drop_duplicates()
df = df.fillna(method='ffill').fillna(method='bfill')


# Convert categorical columns to category type
for col in df.select_dtypes(include=['object']).columns:
df[col] = df[col].astype('category')


return df
