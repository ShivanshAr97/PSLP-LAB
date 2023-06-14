import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=np.random.uniform(0, 10, 100)
y=2*x+1+np.random.normal(0, 1,100)

reg = LinearRegression().fit(x.reshape(-1, 1), y)

y_pred = reg.predict(x.reshape(-1, 1))

mean_error = np.mean(np.abs(y - y_pred))

plt.scatter(x,y, alpha=0.6, color="g")
plt.plot(x, y_pred, "-k", label="Regression line")
plt.legend()

plt.show()

print("Mean error", mean_error)


