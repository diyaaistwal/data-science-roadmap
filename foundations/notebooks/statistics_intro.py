# Introduction to Basic Statistics
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = [12, 15, 18, 20, 21, 24, 25, 26, 29, 30]

# Mean and Median
mean = np.mean(data)
median = np.median(data)

# Variance and Standard Deviation
variance = np.var(data)
std_deviation = np.std(data)

# Plot the data
plt.hist(data, bins=5, alpha=0.7, color='blue', edgecolor='black')
plt.title('Histogram of Sample Data')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()

#mean, median, variance, std_deviation
