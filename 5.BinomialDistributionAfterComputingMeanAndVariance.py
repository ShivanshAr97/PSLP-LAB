import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def compute_mean_variance(n, p):
  mean = n * p
  variance = n * p * (1 - p)
  return mean, variance

def fit_binomial_distribution(mean, variance):
  n = mean**2 / variance
  p = mean / n
  x = np.arange(int(n) + 1)
  y = stats.binom.pmf(x, n, p)
  plt.hist(x,
           bins=int(n + 1),
           weights=y,
           alpha=0.5,
           label="Binomial Distribution")
  plt.plot(x, y, label="FittedBinomialDistribution")
  plt.legend()
  return n, p

plt.figure(figsize=(10, 6))
plt.title("Binomial Distributions")
mean, variance = compute_mean_variance(10, 0.5)
fit_binomial_distribution(mean, variance)
mean, variance = compute_mean_variance(20, 0.5)
fit_binomial_distribution(mean, variance)
mean, variance = compute_mean_variance(10, 0.8)
fit_binomial_distribution(mean, variance)
mean, variance = compute_mean_variance(20, 0.8)
fit_binomial_distribution(mean, variance)
plt.show()
