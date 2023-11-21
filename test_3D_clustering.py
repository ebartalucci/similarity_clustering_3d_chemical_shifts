import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import ListedColormap

# Extracted data points (replace with your actual data)
data = [
    ("39 SER", "C", 174.6),
    ("39 SER", "CA", 57.6),
    ("39 SER", "CB", 65.6),
    ("39 SER", "N", 118.5),
    ("40 GLY", "CA", 47.5),
    ("40 GLY", "N", 110.6),
    ("44 SER", "C", 173.2),
    ("44 SER", "CA", 56.8),
    ("44 SER", "CB", 65.5),
    ("44 SER", "N", 122.1)
    # Add more data points...
]

# Create a colormap with a unique color for each amino acid number
amino_acid_numbers = [aa.split()[0] for aa, _, _ in data]
unique_numbers = list(set(amino_acid_numbers))
num_unique_numbers = len(unique_numbers)
color_map = plt.cm.get_cmap('tab20', num_unique_numbers)
cmap = ListedColormap([color_map(i) for i in range(num_unique_numbers)])

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define chemical shift ranges
shift_ranges = {
    "N": (40, 150),
    "C": (0, 200)
}

# Generate a grid of coordinates within the specified chemical shift ranges
c_shift = np.linspace(shift_ranges["C"][0], shift_ranges["C"][1], 100)
n_shift = np.linspace(shift_ranges["N"][0], shift_ranges["N"][1], 100)
C_shift, N_shift = np.meshgrid(c_shift, n_shift)

# Plot a surface grid for the entire chemical shift range
ax.plot_surface(C_shift, C_shift, N_shift, cmap='gray', alpha=0.2)

# Plot data points with unique colors
for i, (aa, atom, shift) in enumerate(data):
    if atom == "C":
        x_range = (0, shift_ranges[atom][1])  # Start from 0 for both carbon axes
        y_range = (0, shift_ranges[atom][1])
        z_range = (shift_ranges["N"][0], shift_ranges["N"][1])  # Start from N's lower limit

        x = x_range[0] + (x_range[1] - x_range[0]) * (shift - x_range[0]) / (x_range[1] - x_range[0])
        y = y_range[0] + (y_range[1] - y_range[0]) * (shift - y_range[0]) / (y_range[1] - y_range[0])
        z = z_range[0] + (z_range[1] - z_range[0]) * (shift - z_range[0]) / (z_range[1] - z_range[0])

        aa_number = aa.split()[0]
        ax.scatter(x, y, z, c=[cmap(unique_numbers.index(aa_number))], marker='o', label=aa)

# Add colorbar
sm = plt.cm.ScalarMappable(cmap=cmap)
sm.set_array([])
plt.colorbar(sm, label='Amino Acid Number')

ax.set_xlabel('Chemical Shift (C)')
ax.set_ylabel('Chemical Shift (C)')
ax.set_zlabel('Chemical Shift (N)')

plt.show()
