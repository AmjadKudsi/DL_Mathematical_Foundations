# calculate the total sales for each week by adding the corresponding sales data using vector addition

import numpy as np

product_A_sales = np.array([120, 150, 100, 90])
product_B_sales = np.array([80, 60, 75, 110])

# TODO: Calculate and print total sales per week 
print("Weekly Total Sales: ", product_A_sales+product_B_sales)