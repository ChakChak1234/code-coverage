import os, sys
import pandas as pd
import numpy as np

def make_variable_data(n_rows = 1000, dist_type = 'normal'):
    """
    This function generates a variable of n_rows of various distributions
    :param n_rows: number of rows
    :param dist_type: distribution type
    :return: array of values
    """
    if dist_type == 'normal':
        mu = np.random.choice(range(0, 20), 1)[0]
        sigma = 1
        var_values = np.random.normal(loc=mu, scale=sigma, size=n_rows)
    if dist_type == 'uniform':
        uniform_params = sorted(np.random.choice(range(0, 20), 2))
        left = uniform_params[0]
        right = uniform_params[1]
        var_values = np.random.uniform(low=left, high=right, size=n_rows)
    if dist_type == 'poisson':
        exp_val = np.random.choice(range(1, 20))#[0]
        var_values = np.random.poisson(lam=exp_val, size=n_rows)
    if dist_type == 'triangular':
        tri_params = sorted(np.random.choice(range(0, 100), 3))
        left = tri_params[0]
        mode = tri_params[1]
        right = tri_params[2]
        var_values = np.random.triangular(left=left, mode=mode, right=right, size=n_rows)
    if dist_type == 'wald': # Inverse Gaussian
        wald_params = sorted(np.random.choice(range(1, 20), 2))
        mu = wald_params[1]
        scale = wald_params[0]
        var_values = np.random.wald(mean=mu, scale=scale, size=n_rows)
    if dist_type == 'weibull':
        shape = np.random.choice(range(1, 20), 1)[0]
        var_values = np.random.weibull(a=shape, size=n_rows)
    if dist_type == 'categorical':
        n_levels = np.random.choice(range(5, 25))
        var_values = np.random.choice(a=n_levels, size=n_rows)

    return var_values


def make_dataset(n_variables = 7, n_rows = 1000):
    """
    This function returns a dataset of n_variables of various distributions
    :param n_variables: number of variables to create
    :param n_rows: number of rows
    :return: dataset of simulated distributions
    """
    df = pd.DataFrame()

    dist_list = np.random.choice(['normal', 'uniform', 'poisson', 'triangular', 'wald', 'weibull', 'categorical'],
                                 size = n_variables, replace = True)

    count = 1
    for variable in dist_list:
        data = make_variable_data(n_rows = n_rows, dist_type = variable)
        df[variable + '_' + str(count)] = data
        count += 1

    return df
