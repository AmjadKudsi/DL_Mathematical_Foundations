# calculate the net change in prices after applying following two operations

import numpy as np

# Original prices
original_prices = np.array([10, 20, 30])

# TODO: Calculate the percentage increase (20%) using scalar multiplication
percentage_increase = original_prices * 0.2

print("Percent Increase: ", percentage_increase)

# Fixed increase
fixed_increase = np.array([5, 3, 8])

# TODO: Calculate final prices by adding fixed_increase to original_prices
final_prices = fixed_increase + original_prices

print("Final Prices:", final_prices)