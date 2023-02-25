import matplotlib.pyplot as plt
import numpy as np
from GroupActionQuicksort import GroupActionQuicksort

# Generate a random array of 10000 integers between 0 and 10000
arr = np.random.randint(0, 10000, size=10000)

# Plot the array before sorting
plt.subplot(2, 1, 1)
plt.plot(arr)

# Sort the array using GroupActionQuicksort
GroupActionQuicksort(arr)

# Plot the array after sorting
plt.subplot(2, 1, 2)
plt.plot(arr)

# Show the plot
plt.show()
