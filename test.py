import pandas as pd
import numpy as np

df1 = pd.read_csv('coursera-course-data.csv')
df2 = pd.read_csv('coursera-data-full.csv')

#print(df1.head())
print(list(set(df1.Link) - set(df2.Url)))

df2.drop(df2.columns[0], axis=1, inplace=True)
print(df2.head())

df2.to_csv('coursera-data.csv')
