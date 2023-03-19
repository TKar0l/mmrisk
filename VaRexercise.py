

for i in range (1,10_000):
   s = np.random.normal(mu, sigma, 250)
   mu_hat = statistics.mean(s)
   sigma_hat = statistics.stdev(s)
   _VaR_99 = var_emp(s)
   tablica.append(_VaR_99)


print(f'Wartosc oczekiwana:{np.mean(tablica)} ,\nStandard dev: {statistics.stdev(tablica)}')


# tablica2 = []
# for i in range (1,10_000):
#    s = np.random.normal(mu, sigma, 250)
#    temp_mu_hat = statistics.mean(s)
#    temp_sigma_hat = statistics.stdev(s)
#    _VaR_99 = -(temp_mu_hat + temp_sigma_hat*norm.ppf(1-0.99, mu, sigma))
#    tablica2.append(_VaR_99)
#
# print(f' Dla estymatora normalnego: \nWart.ocz: {statistics.mean(tablica2)}\nStd.dev: {statistics.stdev(tablica2)}')

# s = np.random.normal(mu, sigma, 500)
# VaR_99 = norm.ppf(1-0.99, mu_hat, sigma_hat)

# licznik = 0
# tablica = []
# pl = []
# for i in range(0,249):
#    temp = s[i: 249+i]
#    mu_hat = statistics.mean(temp)
#    sigma_hat = statistics.stdev(temp)
#    _VaR_99 = -norm.ppf(1 - 0.99, mu_hat, sigma_hat)
#    tablica.append(_VaR_99)

#    if(s[250+i] > _VaR_99): licznik = licznik+1
#    pl.append(s[250+i] - temp[249+i])


# plt.plot(pl)
# print(f'Wartosc Var: {statistics.mean(tablica)}\nIlosc przekroczen VaRu :{licznik}')