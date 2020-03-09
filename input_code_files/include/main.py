import os, sys
import pandas as pd

import generate_data as generate_data
from make_data_missing import simulate_missing

def main_func():
    df = generate_data.make_dataset(n_variables=7, n_rows=1000)
    for col in df.columns:
        if 'categorical' in str(col):
            df[col] = df[col].astype('category', copy=False)
    df.to_csv('df_complete.csv', header=True, index=False)


    sim_missing = simulate_missing(df = df, conditions = ['missing_rows', 'missing_at_random'])
    df2 = sim_missing.make_data_missing(percent_missing = .3)
    for col in df.columns:
        if 'categorical' in str(col):
            df[col] = df[col].astype('category', copy=False)

    df2.to_csv('df_missing.csv', header=True, index=False)

if __name__ == "__main__":
    main_func()