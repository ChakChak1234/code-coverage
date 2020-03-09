import os, sys
from multiprocessing import Process
import pandas as pd

df_list = []

class main_wrapper():
    def __init__(self, df_list = df_list, *args, **kwargs):
        super(main_wrapper, self).__init__()
        for file in df_list:
            if 'complete' in file:
                file_path = file
                self.df_complete = pd.read_csv(file_path, header=0, sep=',')
                for col in self.df_complete.columns:
                    if 'categorical' in str(col):
                        self.df_complete[col] = self.df_complete[col].astype('category', copy=False)
            if 'missing' in file:
                file_path = file
                self.df_missing = pd.read_csv(file_path, header=0, sep=',')

        self.data = {}
        self.data['Complete'] = self.df_complete.to_dict('list')
        self.data['Algorithms'] = {}
        self.data['Algorithms']['Apriori'] = {}
        self.data['Algorithms']['FpGrowth'] = {}
        self.data['Algorithms']['Inverse_Sampling'] = {}
        self.data['Algorithms']['Multiple_Imputations'] = {}
        self.data['Algorithms']['Variational_Autoencoder'] = {}
        self.data['Algorithms']['Bayesian_Network'] = {}

    def _Apriori(self):
        from Apriori.main import Apriori
        self.Apriori = Apriori(df = self.df_missing)
        apriori = self.Apriori
        result = apriori.run()

    def _FpGrowth(self):
        from FpGrowth.main import FpGrowth
        self.FpGrowth = FpGrowth(df = self.df_missing)
        fpgrowth = self.FpGrowth
        result = fpgrowth.run()

    def _InverseSample(self):
        """
        This function performs inverse transform sampling to generate data
        """
        from InverseSample.main import InverseSampling
        self.InverseSampling = InverseSampling(df = self.df_missing)
        inverse_sample = self.InverseSampling
        inverse_sample_df = inverse_sample.run()

        for col in inverse_sample_df.columns:
            if 'categorical' in str(col):
                inverse_sample_df[col] = inverse_sample_df[col].astype('category', copy=False)

        self.data['Algorithms']['Inverse_Sampling'] = inverse_sample_df.to_dict('list')

        #return self.data['Algorithms']['Inverse_Sampling']

    def _MultipleImputations(self):
        """
        This function performs Multiple Imputations on the missing data
        """
        from MultipleImputations.main import MultipleImputations
        self.MultipleImputations = MultipleImputations(df = self.df_missing)
        multi_impute = self.MultipleImputations
        imputed_df = multi_impute.run()

        for col in imputed_df.columns:
            if 'categorical' in str(col):
                imputed_df[col] = imputed_df[col].astype('category', copy=False)

        self.data['Algorithms']['Multiple_Imputations'] = imputed_df.to_dict('list')

        #return self.data['Algorithms']['Multiple_Imputations']

    def run(self):
        """
        This function runs all data generation algorithms
        """

        # algo_apriori = Process(target = main_wrapper(df_list = df_list)._Apriori)
        # algo_apriori.start()
        #
        # algo_fpgrowth = Process(target = main_wrapper(df_list = df_list)._FpGrowth)
        # algo_fpgrowth.start()

        # algo_inverse_sampling = Process(target = self._InverseSample())
        # algo_inverse_sampling.start()
        self._InverseSample()

        # algo_multi_impute = Process(target=self._MultipleImputations())
        # algo_multi_impute.start()
        self._MultipleImputations()

        return self.data

if __name__ == '__main__':
    import os

    input_code_file_path = str(os.path.join(os.path.abspath(os.getcwd()), 'input_code_files', 'include').replace('\\', '/'))

    df_path = input_code_file_path

    df_list = [(df_path + '/' + i) for i in os.listdir(df_path) if '.csv' in i]

    results = main_wrapper(df_list = df_list).run()
    print(results)



