import pandas as pd
import numpy as np
df = pd.read_csv('Test Data Sheet.csv', engine='c', encoding='utf-8')

print(df.isnull().sum())
df.fillna(df.mean(), inplace=True)

def detect_outliers(col):
    Q1 = np.percentile(col, 25)
    Q3 = np.percentile(col, 75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = find_outliers(col, lower_bound, upper_bound)
    return outliers

def find_outliers(col, lower_bound, upper_bound):
    outliers = []
    for x in col:
        if (x < lower_bound) or (x > upper_bound):
            outliers.append(x)
    return outliers

outliers_hs = detect_outliers(df['home_score'])
outliers_as = detect_outliers(df['away_score'])
df = df[~df['home_score'].isin(outliers_hs)]
df = df[~df['away_score'].isin(outliers_as)]

print(df)