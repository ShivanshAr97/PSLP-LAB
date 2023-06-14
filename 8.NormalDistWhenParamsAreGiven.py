import matplotlib.pyplot as plt
import numpy as np

def plot (mu, sigma):
  x= np. linspace (mu - 3* sigma, mu + 3* sigma, 100)
  y= 1/(sigma * np.sqrt(2* np.pi))*np.exp(-(x-mu)**2/(2*sigma **2))
  plt.plot (x,y, label = f "mu = {mu}, sigma = {sigma}")

plt. figure (figsize = (10,6))
plt. title ("normel Distributions")
plot (0,1)
plot (1,1)
plot (0,2)
plt.legend() 
plt.show()