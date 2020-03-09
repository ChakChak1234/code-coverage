import os, sys, copy
import impyute
import numpy as np
import pandas as pd
import importlib

class MultipleImputations:
    def __init__(self, df, *args, **kwargs):
        super(MultipleImputations, self).__init__()
        self.df = df

    def run(self):

        df, df_len = self.df, len(self.df)
        df_complete, df_len_complete = self.df.dropna(how='all'), len(self.df.dropna(how='all'))

        arr_final = df_complete.to_numpy()
        arr_gen = df.to_numpy()
        sample_size = int(arr_gen.shape[0] * .25)
        arr_final_len = arr_final.shape[0]

        while arr_final_len < df_len:
            arr_sample = arr_gen[np.random.choice(arr_gen.shape[0], sample_size, replace=True), :]
            if np.isnan(arr_sample).any():
                data_gen = impyute.imputation.cs.mice(arr_sample)
                arr_final = np.append(arr_final, data_gen, axis=0)
                arr_final = np.unique(arr_final, axis=0)
                arr_final_len = arr_final.shape[0]

        result_df = pd.DataFrame(data = arr_final,
                                 index=[i for i in range(arr_final.shape[0])],
                                 columns=[str(i) for i in self.df.columns])

        return result_df