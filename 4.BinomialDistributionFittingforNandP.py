# 1.
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.kdeplot(np.random.binomial(20,0.5,1000))
sns.kdeplot(np.random.binomial(40,0.5,1000))
sns.kdeplot(np.random.binomial(40,0.7,1000))

plt.legend(labels=['n=20, p=0.5', 'n=40, p=0.5', 'n=40, p=0.7'])
plt.show()


# 2. 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


#Fit Binomial distibution with given n and p
def fit_binomial_distribution(n, p):
  x = np.arange(n + 1)
  y = stats.binom.pmf(x, n, p)
  #Plot the histogram and the fitted distribution
  plt.hist(x, bins=n, weights=y, alpha=0.5, label="Binomial Distribution")
  plt.plot(x, y, label="Fitted Binomial Distribution")
  plt.legend()


#Fit Binomial distribution with different value of n and p
plt.figure(figsize=(10, 6))
plt.title("Binomial Distribution")
fit_binomial_distribution(10, 0.5)
fit_binomial_distribution(20, 0.5)
fit_binomial_distribution(10, 0.8)
fit_binomial_distribution(20, 0.5)
plt.show()