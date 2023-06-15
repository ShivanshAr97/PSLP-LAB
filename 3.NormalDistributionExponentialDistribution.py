# 1.
import matplotlib.pyplot as plt
import numpy as np

def plot_normal_dist(mu, sigma):
  x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
  y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(1 - (x - mu)**2 /(2 * sigma**2))
  plt.plot(x, y, label=f"mu = {mu}; sigma = {sigma}")


plt.figure(figsize=(10, 6))
plt.title("Normal Distributions")
plot_normal_dist(0, 1)
plot_normal_dist(1, 1)
plot_normal_dist(0, 2)
plt.legend()

plt.show()


# 2.
import matplotlib.pyplot as plt
import numpy as np

def plot_exponential_dist(lamb):
  x = np.linspace(0,5/lamb,100)
  y = lamb*np.exp(-lamb*x)
  plt.plot(x, y, label=f"lambda={lamb}")

plt.figure(figsize=(10, 6))
plt.title("Exponential Distributions")
plot_exponential_dist(1)
plot_exponential_dist(2)
plot_exponential_dist(0.5)
plt.legend()

plt.show()

