import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# 1) Load the CSV data
file_path = r"C:\Users\thvic\Desktop\Lab Report\CMOD\data2.csv"
df = pd.read_csv(file_path)

# Ensure the CSV has the necessary columns: 'Deflection' and 'Load'
if not {"Deflection", "Load"}.issubset(df.columns):
    raise ValueError("CSV must contain columns 'Deflection' and 'Load'.")

# 2) Extract data and sort if necessary
deflection = df['Deflection'].values
load = df['Load'].values

# Sort data by deflection if not strictly increasing
sorted_indices = np.argsort(deflection)
deflection = deflection[sorted_indices]
load = load[sorted_indices]

# 3) Apply a smoothing spline to the entire dataset
# The smoothing factor 's' determines the trade-off between closeness to the data and smoothness.
# Increase s_value to get a smoother curve.
s_value = 1.55e4  # Adjust this value as needed
spline = UnivariateSpline(deflection, load, s=s_value)

# Evaluate the spline at the original deflection points (for full curve)
smoothed_load = spline(deflection)

# 4) Resample the smoothed curve on a uniform grid (without discarding the overall shape)
num_points = 200  # Number of points you want in the reduced representation
deflection_resampled = np.linspace(deflection[0], deflection[-1], num_points)
smoothed_load_resampled = spline(deflection_resampled)

# 5) Compute the area under the resampled smooth curve using trapezoidal integration
area_under_curve = np.trapz(smoothed_load_resampled, deflection_resampled)
print("Area under the curve:", area_under_curve)

# 6) Save the resampled data (and optionally the computed area) to an Excel file
df_resampled = pd.DataFrame({
    "Deflection_Resampled": deflection_resampled,
    "Smoothed_Load_Resampled": smoothed_load_resampled
})
output_excel = "resampled_smoothed_curve.xlsx"
df_resampled.to_excel(output_excel, index=False)
print(f"Resampled smoothed curve has been saved to '{output_excel}'.")

# 7) Plot the raw data, full spline-smoothed curve, and the resampled points
plt.figure(figsize=(10, 6))
plt.plot(deflection, load, 'o', label="Raw Data", markersize=2, alpha=0.5)
plt.plot(deflection, smoothed_load, 'r-', linewidth=2, label="Spline Smoothed (Full Data)")
plt.plot(deflection_resampled, smoothed_load_resampled, 'ko', label="Resampled Points", markersize=4)
plt.xlabel("Deflection (mm)")
plt.ylabel("Load (kN)")
plt.title("Load–Deflection Curve with Spline Smoothing and Resampling")
plt.legend()
plt.grid(True)
plt.show()

