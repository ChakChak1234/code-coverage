import os, sys
import pandas as pd

def read_data(input_file = 'df_complete.csv'):
    input_file = os.path.join('/include', input_file)
    df = pd.read_csv(input_file, headers = True)
    return df

def test_function(df):
    for col in df.columns:
        if 'obj' in str(df[col].dtypes):
            if df[col].mean() > 5:
                return 'Object, mean greater than 5.'
            elif df[col].mean() < 4:
                return 'Object, mean less than 4.'
            else:
                return 'Object, mean between 4 and 5.'
        elif 'int' in str(df[col].dtypes):
            if df[col].mean() > 5:
                return 'Integer, mean greater than 5.'
            elif df[col].mean() < 4:
                return 'Integer, mean less than 4.'
            else:
                return 'Integer, mean between 4 and 5.'
        elif 'float' in str(df[col].dtypes):
            if df[col].mean() > 5:
                return 'Float, mean greater than 5.'
            elif df[col].mean() < 4:
                return 'Float, mean less than 4.'
            else:
                return 'Float, mean between 4 and 5'
        else:
            return 'Dead Line'

if __name__ == "__main__":
    import glob

    list_csv = glob.glob('/include/*.csv')

    count = 1
    for file in list_csv:
        input_data = read_data(input_file = file)
        test_function(input_data)
        count += 1

    if count <= 2:
        print('Done')
    else:
        print('Dead Code')