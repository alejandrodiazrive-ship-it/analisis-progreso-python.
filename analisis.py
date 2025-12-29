import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mi_progreso.csv')
print(df)
print(df.describe())

df['ratio'] = df['total_productivo'] / df['yt_min']
print(f"Ratio promedio: {df['ratio'].mean():.2f}")
print(f"Mejor ratio: {df['ratio'].max():.2f} el {df.loc[df['ratio'].idxmax(), 'fecha']}")