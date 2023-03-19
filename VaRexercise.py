import statistics

import matplotlib.pyplot as plt
import numpy as np
import estimator

mu = 1.0
sigma = np.sqrt(10)

def varSym(samplesize=250, nruns=10_000, alfa=0.01, mu=0.0, sigma=1.0):
    """This function makes nruns simulations to estimate Value at Risk"""
    varTable = []
    for j in range(1, nruns):
        data = np.random.normal(mu, sigma, samplesize)
        var = estimator.var_unorm(data, alfa)
        varTable.append(var)
    return {"meanVar": statistics.mean(varTable),
            "std_dev": statistics.stdev(varTable),
            "nruns": nruns,
            "confLvl": alfa}


# symulacja = varSym(mu = 1.0, sigma = np.sqrt(10))
# print(symulacja)

def breachSym(data, days=250):
    empCount, normCount = 0, 0
    empirical, normal = [], []

    for i in range(1, days + 1):
        temp = data[i - 1:days - 1 + i]

        emp = estimator.var_emp(temp, alfa=0.01)
        norm = estimator.var_unorm(temp, alfa=0.01)

        empirical.append(emp)
        normal.append(norm)

        if (emp < data[days - 1 + i]): empCount = empCount + 1
        if (norm < data[days - 1 + i]): normCount = normCount + 1

    return {"empBreach": empCount,
            "normBrach": empCount,
            "empVar": empirical,
            "normVar": normal,
            "profitLoss": data[-days:]}


#data = np.random.normal(mu, sigma, 500)
#symulacja = breachSym(data)
#print(symulacja.keys())
#print(symulacja["empBreach"])

tmp_emp = []
tmp_norm = []
for i in range(1, 100):
    data = np.random.normal(mu, sigma, 500)
    symulacja = breachSym(data)
    tmp_emp.append(symulacja["empBreach"])
    tmp_norm.append(symulacja["normBrach"])

print(f'{statistics.mean(tmp_emp)}\n{statistics.mean(tmp_emp)}')

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
