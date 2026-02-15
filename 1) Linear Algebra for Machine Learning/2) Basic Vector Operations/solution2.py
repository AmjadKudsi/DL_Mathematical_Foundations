# predict next month's expenses given a fixed inflation rate
# multiply each element of the expense vector by the scalar (1 + inflation_rate)

import numpy as np

expenses = np.array([200, 150, 50, 80])
inflation_rate = 0.03
# TODO: increase expenses based on the suggested inflation rate. Print the new expenses

print("Increased expenses: ", expenses*1.03)
