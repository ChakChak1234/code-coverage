import os, sys
import numpy as np
import pandas as pd
import copy

import generate_data as generate_data

class simulate_missing:
    """

    """
    def __init__(self, df, conditions):
        """

        :param df:
        :param conditions:
        """
        self.df = df
        self.conditions = conditions

    def _missing_at_random(self):
        """
        This function randomly replaces a percentage of the values in the dataframe
        :return:
        """
        df = copy.copy(self.df)

        for col in df.columns:
            df[col] = df[col].sample(frac=self.percent_by_condition)
        self.df = df
        return self.df

    def _missing_columns(self):
        """

        :return:
        """
        return self.df

    def _missing_rows(self):
        """
        This function replaces a percent of the rows in the dataframe with empty rows
        :return:
        """
        df = copy.copy(self.df)
        percent_to_keep = 1 - self.percent_by_condition
        df_len = len(df.index)
        sub_df = df.sample(frac=percent_to_keep)
        rows_to_fill = df_len - len(sub_df.index)

        for _ in range(rows_to_fill):
            sub_df.loc[sub_df.index.max() + 1] = None

        self.df = sub_df

        return self.df

    def _missing_rows_and_columns(self):
        """

        :return:
        """
        return self.df

    def make_data_missing(self, percent_missing = .3):
        """

        :param percent_missing:
        :return:
        """
        total_percent_missing = percent_missing
        self.percent_by_condition = total_percent_missing / len(self.conditions)

        for condition in self.conditions:

            if condition == 'missing_at_random':
                self.df = self._missing_at_random()

            if condition == 'missing_columns':
                self.df = self._missing_columns()

            if condition == 'missing_rows':
                self.df = self._missing_rows()

            if condition == 'missing_rows_and_columns':
                self.df = self._missing_rows_and_columns()

            else:
                return self.df

        return self.df