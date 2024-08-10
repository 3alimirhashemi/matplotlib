from matplotlib import pyplot as plt
import numpy as np
# print(plt.style.available)
# exit()
plt.style.use('seaborn-v0_8-dark')

age = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_index = np.arange(len(age))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(x_index - width, dev_y,
         width=0.25, color="#9467bd", label="all developer")


plt.bar(x_index, py_dev_y,
        width=0.25, color="#f2a4b6", label="python developer")


plt.bar(x_index + width, js_dev_y,
        width=0.25, color="#34a922", label="js developer")


plt.legend()
plt.xticks(ticks=x_index, labels=age)

plt.title("Age By Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.tight_layout()
plt.grid(True)
plt.show()
