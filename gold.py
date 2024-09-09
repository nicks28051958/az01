import pandas as pd

df = pd.read_csv('Gold Price Prediction.csv')
print(df.head(3))
print(df.info())
print(df.describe())