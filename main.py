
import pandas as pd

df = pd.read_csv('dz.csv')


# Группировка по городу и вычисление среднего только для числовых данных
group = df.groupby('City')['Salary'].mean()
print("\nСредние значения по зарплате:")
print(group)
