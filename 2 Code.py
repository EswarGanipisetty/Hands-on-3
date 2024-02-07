
import time
import matplotlib.pyplot as plt
import numpy as np

def f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
    return x

# Set up values of n
n_values = np.arange(1, 101)  # Adjust the range as needed

# Measure execution time for each n
times = []
for n in n_values:
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    times.append(elapsed_time)

# Plot the results
plt.plot(n_values, times, label='Execution Time')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Algorithm Runtime for Different Values of n')
plt.legend()

# Fit a polynomial curve
coefficients = np.polyfit(n_values, times, 2)  # Change the degree as needed
poly_fit = np.poly1d(coefficients)
plt.plot(n_values, poly_fit(n_values), '--', label='Curve Fit')

# Show the plot
plt.show()
