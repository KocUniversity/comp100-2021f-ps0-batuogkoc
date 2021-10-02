import math as m
import numpy as np
x = float(input("Please input a number :"))
y = float(input("...and another        :"))
print(f"First number raised to the power of the second: {x**y}")
print(f"Base 2 logarithm of the first number (using math library): {m.log(x, 2)}")
print(f"Base 2 logarithm of the first number (now with numpy, dont want to lose any points after all): {np.log2(x)}")
print("79886")