import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# ---------------------------------------------------------------------
# 1) Hard-coded data (Deflection_Resampled, Smoothed_Load_Resampled)
data_str = """Deflection_Resampled	Smoothed_Load_Resampled
0	0
0.049891174	15.89670418
0.05	16
0.060298851	16.39412463
0.080547719	19.0118684
0.100796586	21.32041118
0.121045453	23.34573842
0.14129432	25.11383555
0.161543187	26.650688
0.181792054	27.98228121
0.202040922	29.12948248
0.222289789	30.08737612
0.242538656	30.8429457
0.262787523	31.38317189
0.28303639	31.69503533
0.300292641	31.77080728
0.303285257	31.76551668
0.323534125	31.5815966
0.343782992	31.14028317
0.364031859	30.54268936
0.384280726	29.95161181
0.404529593	29.53065484
0.42477846	29.41272823
0.445027328	29.54748065
0.465276195	29.81683635
0.485525062	30.10960617
0.505773929	30.38510303
0.526022796	30.64346594
0.546271663	30.88533261
0.566520531	31.11134074
0.586769398	31.32212805
0.607018265	31.51833226
0.627267132	31.70059108
0.647515999	31.86954222
0.667764866	32.02582341
0.688013733	32.17007234
0.708262601	32.30292674
0.728511468	32.42502432
0.748760335	32.5370028
0.769009202	32.63949989
0.789258069	32.73315329
0.809506936	32.81860074
0.829755804	32.89647994
0.850004671	32.9674286
0.870253538	33.03208443
0.890502405	33.09108517
0.910751272	33.14506851
0.931000139	33.19467217
0.951249007	33.24053386
0.971497874	33.28329131
0.991746741	33.32358221
1.011995608	33.3620443
1.032244475	33.39931527
1.052493342	33.43603285
1.07274221	33.47282777
1.092991077	33.51003584
1.113239944	33.54759554
1.133488811	33.58541735
1.153737678	33.62341174
1.173986545	33.66148915
1.194235412	33.69956006
1.21448428	33.73753493
1.234733147	33.77532422
1.254982014	33.81283841
1.275230881	33.84998794
1.295479748	33.88668329
1.315728615	33.92283491
1.335977483	33.95835328
1.35622635	33.99314886
1.376475217	34.02713211
1.396724084	34.06021349
1.416972951	34.09230347
1.437221818	34.12331251
1.457470686	34.15315107
1.477719553	34.18172963
1.49796842	34.20895863
1.5	34.23474856
1.538466154	34.25900986
1.558715021	34.28165301
1.578963889	34.30258846
1.599212756	34.32172669
1.619461623	34.33897815
1.63971049	34.35425331
1.659959357	34.36746265
1.680208224	34.37854185
1.700457092	34.38750641
1.720705959	34.39438754
1.740954826	34.39921646
1.761203693	34.4020244
1.78145256	34.40284258
1.801701427	34.40170222
1.821950294	34.39863455
1.842199162	34.39367078
1.862448029	34.38684213
1.882696896	34.37817984
1.902945763	34.36771511
1.92319463	34.35547917
1.943443497	34.34150325
1.963692365	34.32581856
1.983941232	34.30845633
2.004190099	34.28944777
2.024438966	34.26882412
2.044687833	34.24661659
2.0649367	34.2228564
2.085185568	34.19757477
2.105434435	34.17080294
2.125683302	34.14257211
2.145932169	34.11291351
2.166181036	34.08185837
2.186429903	34.0494379
2.206678771	34.01568332
2.226927638	33.98062586
2.247176505	33.94429674
2.267425372	33.90672718
2.287674239	33.86794841
2.307923106	33.82799163
2.328171973	33.78688809
2.348420841	33.74466899
2.368669708	33.70136556
2.388918575	33.65700903
2.409167442	33.6116306
2.429416309	33.56526151
2.449665176	33.51793298
2.469914044	33.46967623
2.490162911	33.42052247
2.5	33.37050294
"""

# ---------------------------------------------------------------------
# 2) Parse the data
data_file = StringIO(data_str)
arr = np.loadtxt(data_file, skiprows=1)
x_all = arr[:, 0]
y_all = arr[:, 1]

# ---------------------------------------------------------------------
# 3) Define the special points for this new polygon:
#   We want to find the area enclosed by:
#   - The line joining A = (0.045032501, 2.699260101) to B = (0.5, 0)
#   - The line from B = (0.5, 0) to C = (1.5, 0)
#   - The point D on the curve at x = 1.5, which is given as (1.5, 32.23513042)
#   - And then the actual curve from (1.5, 32.23513042) back to A (following the experimental data)
A = (0.05,16)
B = (0.5, 0)
C = (1.5, 0)
D = (1.5,34.23474856)

# ---------------------------------------------------------------------
# 4) Extract the curve between x = 0.045032501 and x = 1.5 from the data
x_min = A[0]
x_max = C[0]  # 1.5
N = 100  # number of sample points along the curve
x_curve = np.linspace(x_min, x_max, N)
y_curve = np.interp(x_curve, x_all, y_all)

# ---------------------------------------------------------------------
# 5) Build the polygon in order:
#    The polygon vertices (in order) will be:
#       A  ->  B  ->  C  ->  D  ->  (the curve from x=1.5 back to x=0.045) -> A
poly_points = []
poly_points.append(A)  # A
poly_points.append(B)  # B
poly_points.append(C)  # C
poly_points.append(D)  # D

# Now add the curve points from x=1.5 down to x=0.045 (reversed order)
for i in range(N):
    idx = N - 1 - i
    pt = (x_curve[idx], y_curve[idx])
    # Avoid duplicating A and D
    if np.allclose(pt, D, atol=1e-8) or np.allclose(pt, A, atol=1e-8):
        continue
    poly_points.append(pt)

# Close the polygon by returning to A
poly_points.append(A)

# Convert polygon points to a NumPy array
poly_arr = np.array(poly_points)
px = poly_arr[:, 0]
py = poly_arr[:, 1]

# ---------------------------------------------------------------------
# 6) Compute the area using the shoelace formula
area = 0.5 * abs(np.dot(px, np.roll(py, -1)) - np.dot(py, np.roll(px, -1)))
print(f"Enclosed Area = {area:.3f} kN·mm")

# ---------------------------------------------------------------------
# 7) Plot the results
plt.figure(figsize=(10, 6))

# Plot the full experimental curve in black (for reference)
plt.plot(x_all, y_all, label="Full Data")

# Plot the polygon and fill it with a transparent color
plt.fill(px, py, color='cyan', alpha=0.4, label="Enclosed Region")

# Draw the boundary lines for the polygon
# Line A->B
plt.plot([A[0], B[0]], [A[1], B[1]], 'r--', lw=2, label="Line A→B")
# Line B->C
plt.plot([B[0], C[0]], [B[1], C[1]], 'r--', lw=2, label="Line B→C")
# (Vertical line from C to D is not needed as C and D share x=1.5, but we can mark it)
plt.plot([C[0], D[0]], [C[1], D[1]], 'r--', lw=2, label="Line C→D")

# Plot the curve segment (A to D) in green
plt.plot(x_curve, y_curve, 'g-', lw=2, label="Curve (A→D)")

# Mark special points
for point, lbl in zip([A, B, C, D], ["A", "B", "C", "D"]):
    plt.scatter(point[0], point[1], color='red', s=80, zorder=5)
    plt.text(point[0], point[1], lbl, color='red', fontsize=12)

# Annotate the computed area on the plot
plt.text(0.7, 10, f"Area = {area:.3f} kN·mm", color='purple', fontsize=12)

plt.xlabel("Deflection (mm)")
plt.ylabel("Load (kN)")
plt.title("Enclosed Area using CMOD Curve and Special Lines")
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()
