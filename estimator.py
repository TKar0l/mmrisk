import numpy as np
import statistics
from scipy.stats import norm, t

''' In this script I will implement three Value at Risk estimators such as:
1) Empieical estimator
2) Normal estimator
3) Unbiased normal estimator
'''


# Empirical estimator
def var_emp(data, alfa=0.01):
    """Empirical Value at Risk estimator
    alfa - confidence level (by default 1%)
    data - is our set with our observations"""
    mu_hat = statistics.mean(data)  # empirical mean
    sigma_hat = statistics.stdev(data)  # empirical standard deviation
    empVar = -norm.ppf(alfa, mu_hat, sigma_hat)
    return empVar


# Normal estimator
def var_norm(data, alfa=0.01):
    """Value at Risk normal estimator
    alfa - confidence level (by default 1%
    data - dataset with our observations"""
    mu_hat = statistics.mean(data)  # empirical mean
    sigma_hat = statistics.stdev(data)  # empirical standard deviation
    return -(mu_hat + sigma_hat * norm.ppf(alfa))


# Unbiased normal estimator

def var_unorm(data, alfa=0.01):
    """Unbiased normal estimator of Value at Risk"""
    mu_hat = statistics.mean(data)  # empirical mean
    sigma_hat = statistics.stdev(data)  # empirical standard deviation
    n = len(data)  # number of observations
    return -(mu_hat + sigma_hat * np.sqrt((n + 1) / n) * (t.ppf(alfa, n - 1)))
