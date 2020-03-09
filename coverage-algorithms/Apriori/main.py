import os, sys
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

class Apriori:
    def __init__(self, df, *args, **kwargs):
        super(Apriori, self).__init__()
        self.df = df

    def transform(self):
        te = TransactionEncoder()
        te_ary = te.fit(self.df).transform(self.df)
        self.df = pd.DataFrame(te_ary, columns=te.columns_)
        return self.df

    def run(self):
        te = TransactionEncoder()
        te_ary = te.fit(self.df).transform(self.df)
        df = pd.DataFrame(te_ary, columns=te.columns_)
        df = apriori(df, min_support=0.05)
        return df