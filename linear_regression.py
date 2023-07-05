# Jackson Small
# July 4, 2023
# Linear Regression calculator

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# asks and creates x - values

print("------ x values ------")
numbers_x = []


while True:
    input_number_x = input("Please enter a number or enter 'q' to quit: ")

    if input_number_x.lower() == 'q':
        break
    try:
        input_number_x = float(input_number_x)
        numbers_x.append(input_number_x)
    except ValueError:
        print("That is not a number. Please enter a number. ")

    x_val = np.array(numbers_x)

print("X - Values:", x_val, sep="\n")

# asks and creates y - values


print("------ y values ------")
numbers_y = []

while True:
    input_number_y = input("Please enter a number or enter 'q' to quit: ")

    if input_number_y.lower() == 'q':
        break
    try:
        input_number_y = float(input_number_y)
        numbers_y.append(input_number_y)
    except ValueError:
        print("That is not a number. Please enter a number. ")

    y_val = np.array(numbers_y)

print("Y - Values:", y_val, sep="\n")

# tests shape

print(np.shape(x_val))
print(np.shape(y_val))

# tests dimensions

# print(x_val.ndim)
# print(y_val.ndim)

# Linear Regression Analysis
if np.shape(x_val) == np.shape(y_val) and x_val.ndim == y_val.ndim:
    plt.plot(x_val, y_val)
    plt.show()
    print("Opening graph...")
elif np.shape(x_val) != np.shape(y_val) or x_val.ndim != y_val.ndim:
    print("The number of x's and y's don't match! Please correct them.")


