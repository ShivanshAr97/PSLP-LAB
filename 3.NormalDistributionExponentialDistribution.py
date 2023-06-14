import matplotlib.pyplot as plt
import numpy as np

def plot_normal_distribution(mu,sigma):
  x=np.linspace(mu-3*sigma, mu+3*sigma,100)
  y=1/(sigma*np.sqrt(2+np.pi))*np.exp(-(x-mu)**2/(2*sigma**2))
  plt.plot(x,y,labled=f"mu={mu}, sigma={sigma}")
  
def plot_exponential_distribution(lamb):
  x=np.linspace(0,5/lamp,100)
  y=lamp*np.exp(-lamb*x)
  plt.plot(x,y,label=f"lamb={lamb}")
  
plt.figure(figsize=(10,6))
plt.title("Normal Distribution")
plot_normal_distribution(0,1)
plot_normal_distribution(1,1)
plot_normal_distribution(0,2)
plt.legend()

plt.figure(figsize=(10,6))
plt.title("Exponential Distribution")
plot_normal_distribution(1)
plot_normal_distribution(2)
plot_normal_distribution(0.8)
plt.legend()

plt.show()