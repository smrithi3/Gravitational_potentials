import numpy as np
from scipy.optimize import minimize

# Constants
G = 6.67430e-11  # Gravitational constant (m^3/kg/s^2)
M1 = 5.972e24  # Mass of the primary body (kg)
M2 = 7.349e22  # Mass of the secondary body (kg)
R = 3.844e8  # Distance between the bodies (m)

# Function to calculate effective potential
def effective_potential(r, L):
    return -G * (M1 + M2) / r + (L ** 2) / (2 * M2 * r ** 2)

# Function to minimize for Lagrange points
def lagrange_eq(x):
    r = x[0]
    return effective_potential(r, 0)  # For Lagrange points, angular momentum is 0

# Find Lagrange points
lagrange_points = []
for x_initial_guess in [R * 0.5, R * 1.5]:
    res = minimize(lagrange_eq, x_initial_guess, bounds=[(R * 0.1, R * 10)])
    lagrange_points.append(res.x[0])

# Print Lagrange points
print("Lagrange Points:", lagrange_points)

# Visualize the effective potential
import matplotlib.pyplot as plt

r_values = np.linspace(R * 0.1, R * 10, 1000)
V_values = effective_potential(r_values, 0)  # For visualization, use L=0
plt.plot(r_values, V_values)
plt.xlabel('Distance (m)')
plt.ylabel('Effective Potential (J/kg)')
plt.title('Effective Gravitational Potential')
plt.grid(True)
plt.show()
