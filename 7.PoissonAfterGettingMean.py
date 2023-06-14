import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import poisson

mean=5
data=np.random.poisson(mean,1000)

mu=np.mean(data)
poisson_fit=poisson(mu)

x=np.arange(poisson.ppf(0.01,mu),poisson.ppf(0.99,mu))

plt.hist(data,bins=30,density=True, alpha=0.6,color='g')
plt.plot(x,poisson_fit.pmf(x), '-k', label="Poisson")

plt.legend()
plt.show()