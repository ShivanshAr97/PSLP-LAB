import numpy as np

def random_num():
  return np.random.random()

def coin_flip():
  return int(random_num()>0.5)
  
def simulate_coin_flips(n):
  heads=0
  for i in range(n):
    heads+=coin_flip()
  return heads/n
  
num_simulations=1000
num_flip=100
sum_of_fractions=0

for i in range(num_simulations):
  sum_of_fractions += simulate_coin_flips(num_flip)
  average_fractions = sum_of_fractions/num_simulations

print("Theoretical prob: 0.5")
print("Observed prob: ", average_fractions)