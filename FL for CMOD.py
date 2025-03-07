
import numpy as np
import matplotlib.pyplot as plt

# Effective depth (h_sp) for CMOD-based strain conversion:
h_sp = 90.0  # mm

# Define CMOD values (mm) for the key points:
cmod_FL = 0.05   # assumed at FL (for stress f_ct,L)
cmod_2  = 0.5    # CMOD for the first residual point
cmod_3  = 2.5    # CMOD for the second residual point

# Compute nominal strains as (CMOD / h_sp):
eps_FL = cmod_FL / h_sp      # ~0.000556
eps_2  = cmod_2  / h_sp      # ~0.005556
eps_3  = cmod_3  / h_sp      # ~0.02778

# Calculated stress values (in N/mm², i.e., MPa):
f_ct_L  = 13.24    # from CMOD-based FL calculation
f_eq_2  = 70.06    # from area D_BZ,2 and F2 calculation
f_eq_3  = 25.41    # from area D_BZ,3 and F3 calculation

# Build arrays for plotting (starting from (0,0))
strain_points = np.array([0.0, eps_FL, eps_2, eps_3])
stress_points = np.array([0.0, f_ct_L, f_eq_2, f_eq_3])

# Plot the stress-strain diagram
plt.figure(figsize=(7,5))
plt.plot(strain_points, stress_points, marker='o', linestyle='-', color='blue', label="Stress-Strain Curve")
for i, (eps, stress) in enumerate(zip(strain_points, stress_points)):
    plt.text(eps, stress, f"({eps:.4f}, {stress:.2f})", fontsize=9, ha='left', va='bottom')

plt.xlabel(r"Nominal Strain, $\varepsilon = \mathrm{CMOD}/h_{sp}$")
plt.ylabel("Stress (N/mm²)")
plt.title("Approximate Stress–Strain Diagram (CMOD-based)")
plt.grid(True)
plt.legend()
plt.show()
