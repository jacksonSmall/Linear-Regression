# Jackson Small
# July 4, 2023
# Linear Regression calculator

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def ask_for_x():
    while True:
        input_number_x = input("x value: ")
        try:
            return float(input_number_x)
        except ValueError:
            print("That is not a number. Please enter a number. ")

def ask_for_y():
    while True:
        input_number_y = input("y value: ")
        try:
            return float(input_number_y)
        except ValueError:
            print("That is not a number. Please enter a number. ")

numbers_x = []
numbers_y = []

pts_len = int(input('How many points do u wanna put in????????????'))

for i in range(pts_len):
    print("Please enter a (x,y) pair ")
    numbers_x.append(ask_for_x())
    numbers_y.append(ask_for_y())


x_val = np.array(numbers_x)
print("X - Values:", x_val, sep="\n")
y_val = np.array(numbers_y)
print("y - Values:", y_val, sep="\n")

plt.scatter(x_val, y_val)
plt.show()
plt.plot(x_val, y_val)
plt.show()

out_arr = np.add(x_val, y_val)

sns.histplot(data=x_val, kde=True, color= 'skyblue')
plt.xlabel("x values")
plt.ylabel("Frequency")
plt.title("x value histogram")
plt.show()