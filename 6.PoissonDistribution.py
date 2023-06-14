import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def fit_poisson_distribution(lam):
  x=np.arange(int(lam)+1)
  y=stats.poisson.pmf(x,lam)
  plt.hist(x,bins=int(lam),weights=y,alpha=0.5,label="Poisson Dist")
  plt.plot(x,y,label="Fitted Poisson Dist")
  plt.legend()
  
plt.figure(figsize=(10,6))
plt.title("Poiison Dist")
fit_poisson_distribution(2)
fit_poisson_distribution(5)
fit_poisson_distribution(3)
fit_poisson_distribution(1)
plt.show()