import timeit
import matplotlib.pyplot as plt
import numpy as np

def modified_function(n):
    x = 1
    y = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x + 1
            y = i + j

# Set up values of n
n_values = np.arange(1, 101)  # Adjust the range as needed

# Measure execution time for each n
times = []
for n in n_values:
    time_taken = timeit.timeit(lambda: modified_function(n), number=1000)  # Adjust the number as needed
    times.append(time_taken)

# Plot the results
plt.figure(figsize=(10, 6))

# Plot the full data
plt.subplot(1, 2, 1)
plt.plot(n_values, times, label='Execution Time')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Modified Function Runtime - Full Data')
plt.legend()

# Fit a polynomial curve
coefficients = np.polyfit(n_values, times, 2)
poly_fit = np.poly1d(coefficients)
plt.plot(n_values, poly_fit(n_values), '--', label='Curve Fit')

# Zoom in on the plot
plt.subplot(1, 2, 2)
plt.plot(n_values, times, label='Execution Time')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Modified Function Runtime - Zoomed In')
plt.xlim(0, 20)  # Adjust the range for zooming
plt.ylim(0, max(times[:20]))  # Adjust the range for zooming
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
