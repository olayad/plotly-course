#!/usr/bin/env python


# Excersice from following videos

import pandas as pd
import numpy as np

df = pd.read_csv('salaries.csv')

print(df)
print()

print(df[['Salary', 'Name']])

print(df['Salary'].min())

bol = df['Age'] < 30
print(bol)
print()
print(df[bol])
print()

mat = np.arange(0, 10).reshape(5, 2)

print(mat)
df = pd.DataFrame(data=mat, columns=['A','B'])
print(df)