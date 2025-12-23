import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers between 1 and 100
random_data = np.random.randint(1, 101, size=50)

# Create a figure and a set of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Visualization of Random Integer Array', fontsize=16)

# Line Chart
axes[0, 0].plot(random_data, color='darkblue', linestyle='-', marker='o', markersize=4)
axes[0, 0].set_title('Line Chart', fontsize=14)
axes[0, 0].set_xlabel('Index', fontsize=12)
axes[0, 0].set_ylabel('Value', fontsize=12)
axes[0, 0].grid(True, linestyle='--', alpha=0.7)

# Scatter Plot
axes[0, 1].scatter(range(len(random_data)), random_data, color='forestgreen', alpha=0.7, s=50)
axes[0, 1].set_title('Scatter Plot', fontsize=14)
axes[0, 1].set_xlabel('Index', fontsize=12)
axes[0, 1].set_ylabel('Value', fontsize=12)
axes[0, 1].grid(True, linestyle=':', alpha=0.6)

# Histogram
axes[1, 0].hist(random_data, bins=10, color='goldenrod', edgecolor='black', alpha=0.8)
axes[1, 0].set_title('Histogram', fontsize=14)
axes[1, 0].set_xlabel('Value Bins', fontsize=12)
axes[1, 0].set_ylabel('Frequency', fontsize=12)
axes[1, 0].grid(axis='y', linestyle='--', alpha=0.7)

# Box Plot
axes[1, 1].boxplot(random_data, vert=False, patch_artist=True, 
                  boxprops=dict(facecolor='lightcoral', color='firebrick'),
                  medianprops=dict(color='black', linewidth=2),
                  whiskerprops=dict(color='firebrick'),
                  capprops=dict(color='firebrick'))
axes[1, 1].set_title('Box Plot', fontsize=14)
axes[1, 1].set_xlabel('Value', fontsize=12)
axes[1, 1].set_yticks([]) # Hide y-axis ticks for better visualization
axes[1, 1].grid(axis='x', linestyle=':', alpha=0.6)

# Adjust layout to prevent overlapping titles/labels
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Display the plots
plt.show()