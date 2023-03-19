import statistics

import matplotlib.pyplot as plt
import numpy as np
import estimator


def varSym(samplesize=250, nruns=10_000, alfa=0.01, mu=0.0, sigma=1.0):
    """This function makes nruns simulations to estimate Value at Risk.
    The purpose was to  compare different estimators """
    varTable = []
    for j in range(1, nruns):
        data = np.random.normal(mu, sigma, samplesize)
        var = estimator.var_unorm(data, alfa)
        varTable.append(var)
    return {"meanVar": statistics.mean(varTable),
            "std_dev": statistics.stdev(varTable),
            "nruns": nruns,
            "confLvl": alfa}

#global mu,sigma = 1.0, np.sqrt(10)

# symulacja = varSym(mu = 1.0, sigma = np.sqrt(10))
# print(symulacja)

def breachSym(data, days=250, alfa=0.01):
    """This function returns number of VaR breaches in a given dataset.
    days - we estimate VaR on past num of days (by default 250) and
    check if we have bigger losses than Value at Risk"""
    empCount, normCount = 0, 0  # Creating counter for Var breaches
    empirical, normal = [], []  # to store Value at Risk

    for i in range(1, days + 1):
        temp = data[i - 1:days - 1 + i]  # we take last "days" amout of days to estimate VaR

        emp = estimator.var_emp(temp, alfa)
        norm = estimator.var_unorm(temp, alfa)

        empirical.append(emp)
        normal.append(norm)

        if (emp < data[days - 1 + i]): empCount = empCount + 1  # checking wether losses were greater than Value at Risk
        if (norm < data[days - 1 + i]): normCount = normCount + 1

    return {"empBreach": empCount,
            "normBreach": empCount,
            "empVar": empirical,
            "normVar": normal,
            "profitLoss": data[-days:]}

mu,sigma = 1.0, np.sqrt(10)
# data = np.random.normal(mu, sigma, 500)
# symulacja = breachSym(data)
# print(symulacja.keys())
# print(symulacja["empBreach"])

def breachMcSym(mu=0.0, sigma=1.0, nruns=100, alfa=0.01, days=250):

    for i in range(1, nruns):
        data = np.random.normal(mu, sigma, 500)
        tmp_emp, tmp_norm = [], []
        symulacja = breachSym(data, days, alfa)
        tmp_emp.append(symulacja["empBreach"])
        tmp_norm.append(symulacja["normBreach"])

    print(f'Avrage number of VaR breaches for\nEmpirical estimator: {statistics.mean(tmp_emp)}\n'
          f'Unbiased normal estimator: {statistics.mean(tmp_emp)}')


#breachMcSym(mu, sigma, nruns=300) #do poprawy, cos nie dziala


# empirical = []
# normal = []
# data = np.random.normal(mu, sigma, 500)
#
# empCount, normCount = 0, 0
# for i in range(1, 251):
#    temp = data[i - 1:249 + i]  # tablica zawierajaca zmiany cen z 250 dni
#
#    emp = estimator.var_emp(temp, alfa=0.01)
#    norm = estimator.var_unorm(temp, alfa=0.01)
#
#    empirical.append(emp)
#    normal.append(norm)
#
#    if (emp < data[250 - 1 + i]): empCount = empCount + 1
#    if (norm < data[250 - 1 + i]): normCount = normCount + 1
#
# print(empCount, normCount)
# plt.plot([-x for x in empirical])
# plt.plot([-x for x in normal])
# plt.plot(tablica[250:501])
# plt.show()
#
