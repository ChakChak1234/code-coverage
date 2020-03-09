import os, sys, copy
import numpy as np
import pandas as pd
import scipy.interpolate as interpolate

class InverseSampling:
    def __init__(self, df, *args, **kwargs):
        super(InverseSampling, self).__init__()
        self.df = df

    def inverse_transform_sampling(data, n_bins=40, n_samples=1000):
        hist, bin_edges = np.histogram(data, bins=n_bins, density=True)
        cum_values = np.zeros(bin_edges.shape)
        cum_values[1:] = np.cumsum(hist * np.diff(bin_edges))
        inv_cdf = interpolate.interp1d(cum_values, bin_edges)
        r = np.random.rand(n_samples)
        return inv_cdf(r)

    def inv_transform_df_simulator(self):
        df, df_len = self.df, len(self.df)
        df_complete, df_len_complete = self.df.dropna(how='all'), len(self.df.dropna(how='all'))

        gen_inv_samp = []

        for col in df_complete.columns:
            col_data = df_complete[col].to_numpy()
            hist, bin_edges = np.histogram(col_data, bins=50, density=True)
            cum_values = np.zeros(bin_edges.shape)
            cum_values[1:] = np.cumsum(hist * np.diff(bin_edges))
            inv_cdf = interpolate.interp1d(cum_values, bin_edges)
            r = np.random.rand(df_len)
            inv_samp_col_data = inv_cdf(r)
            gen_inv_samp.append(inv_samp_col_data)

        gen_inv_samp = np.array(gen_inv_samp, dtype=float)

        return  gen_inv_samp

    def run(self):
        df, df_len = self.df, len(self.df)
        df_complete, df_len_complete = self.df.dropna(how='all'), len(self.df.dropna(how='all'))

        arr_final_len = 0
        arr_final = df_complete.iloc[0:1, :].to_numpy()

        while arr_final_len < df_len:
            arr_gen = self.inv_transform_df_simulator().T

            arr_final = np.append(arr_final, arr_gen, axis=0)
            arr_final = np.unique(arr_final, axis=0)
            arr_final_len += arr_final.shape[0]

        result_df = pd.DataFrame(data = arr_final,
                                 index=[i for i in range(arr_final.shape[0])],
                                 columns=[str(i) for i in self.df.columns])
        return result_df