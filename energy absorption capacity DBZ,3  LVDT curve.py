import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

# ---------------------------------------------------------------------
# 1) Hard-coded data (Deflection_Resampled, Smoothed_Load_Resampled)
data_str = """Deflection_Resampled    Smoothed_Load_Resampled
0	0
0.045032501	2.699260101
0.063232498	2.976538635
0.089457296	3.409525105
0.115682093	3.881323719
0.141906891	4.391177807
0.168131689	4.938330696
0.194356487	5.522025718
0.220581284	6.141506202
0.246806082	6.796015476
0.27303088	7.484796871
0.299255677	8.207093717
0.325480475	8.962149342
0.351705273	9.749207076
0.37793007	10.56751025
0.404154868	11.41630219
0.430379666	12.29482623
0.456604464	13.2023257
0.482829261	14.13801232
0.509054059	15.09878425
0.535278857	16.07769007
0.561503654	17.06741442
0.587728452	18.06064194
0.61395325	19.05005726
0.640178047	20.02834502
0.666402845	20.98818985
0.692627643	21.92227639
0.718852441	22.82328927
0.745077238	23.68391312
0.771302036	24.49683257
0.797526834	25.25473228
0.823751631	25.95029685
0.849976429	26.57621095
0.876201227	27.12515918
0.902426024	27.5898262
0.928650822	27.96301291
0.95487562	28.24460969
0.981100418	28.44556126
1.007325215	28.57777094
1.033550013	28.65314204
1.059774811	28.6835779
1.085999608	28.68098184
1.112224406	28.65725832
1.138449204	28.75213345
1.164674001	29.18889123
1.190898799	29.69965955
1.217123597	30.19610862
1.243348395	30.66673972
1.269573192	31.10009618
1.29579799	31.4847213
1.322022788	31.80915839
1.348247585	32.06195077
1.374472383	32.23372594
1.400697181	32.33067456
1.426921978	32.36602568
1.453146776	32.35304294
1.479371574	32.30498998
1.505596372	32.23513042
1.531821169	32.1567279
1.558045967	32.08304605
1.584270765	32.02734451
1.610495562	31.99904862
1.63672036	31.99660676
1.662945158	32.01651543
1.689169955	32.0552711
1.715394753	32.10937026
1.741619551	32.1753094
1.767844348	32.24975776
1.794069146	32.33096909
1.820293944	32.41804862
1.846518742	32.51010971
1.872743539	32.60626574
1.898968337	32.7056301
1.925193135	32.80731616
1.951417932	32.91043731
1.97764273	33.01410693
2.003867528	33.11743839
2.030092325	33.21954507
2.056317123	33.31954036
2.082541921	33.41653763
2.108766719	33.50965027
2.134991516	33.59815281
2.161216314	33.6819708
2.187441112	33.76119411
2.213665909	33.83591264
2.239890707	33.90621627
2.266115505	33.97219489
2.292340302	34.03393838
2.3185651	34.09153664
2.344789898	34.14507955
2.371014696	34.194657
2.397239493	34.24035888
2.423464291	34.28227506
2.449689089	34.32049545
2.475913886	34.35510992
2.58	34.38620836
2.528363482	34.41388067
2.554588279	34.43821672
2.580813077	34.4593064
2.607037875	34.47723961
2.633262673	34.49210623
2.65	34.50399614
"""

# ---------------------------------------------------------------------
# 2) Parse the data
data_file = StringIO(data_str)
arr = np.loadtxt(data_file, skiprows=1)
x_all = arr[:, 0]
y_all = arr[:, 1]

# ---------------------------------------------------------------------
# 3) Define special points
# A -> B -> C -> D -> (curve from x=2.65 down to x=0.045...) -> A
A = (0.045032501, 2.699260101)   # "left top" point
B = (0.3, 0)                     # next line
C = (2.65, 0)                    # line from (2.65, 34.50399614) down to (2.65,0)
D = (2.65, 34.50399614)

# We'll sample the curve from x=2.65 down to x=0.045, i.e. the entire range [0.045..2.65].
x_min = A[0]
x_max = D[0]

# We'll create a set of points from x=0.045..2.65
N = 200
x_curve = np.linspace(x_min, x_max, N)  # from 0.045 to 2.65
y_curve = np.interp(x_curve, x_all, y_all)

# ---------------------------------------------------------------------
# 4) Build the polygon in order:
#    A -> B -> C -> D -> (curve from x=2.65 down to x=0.045) -> A
poly_points = []
poly_points.append(A)  # A
poly_points.append(B)  # B
poly_points.append(C)  # C
poly_points.append(D)  # D

# Add the curve from x=2.65 down to x=0.045
for i in range(N):
    idx = N - 1 - i
    xx = x_curve[idx]
    yy = y_curve[idx]
    # skip if it's exactly D or A
    # approximate check:
    if abs(xx - D[0]) < 1e-10 and abs(yy - D[1]) < 1e-6:
        continue
    if abs(xx - A[0]) < 1e-10 and abs(yy - A[1]) < 1e-6:
        continue
    poly_points.append((xx, yy))

# Close the polygon by returning to A
poly_points.append(A)

# Convert to array for shoelace
poly_arr = np.array(poly_points)
px = poly_arr[:, 0]
py = poly_arr[:, 1]

# ---------------------------------------------------------------------
# 5) Shoelace formula for area
area = 0.5 * abs(
    np.dot(px, np.roll(py, -1)) - np.dot(py, np.roll(px, -1))
)

print(f"Enclosed Area = {area:.3f} kN·mm")

# ---------------------------------------------------------------------
# 6) Plot
plt.figure(figsize=(10, 6))

# Plot entire data in black
plt.plot(x_all, y_all, label="Full Data")

# Fill the polygon
plt.fill(px, py, color='pink', alpha=0.4, label="Enclosed Polygon")

# Mark lines in red
plt.plot([A[0], B[0]], [A[1], B[1]], 'r--', lw=2, label="Line A→B")
plt.plot([B[0], C[0]], [B[1], C[1]], 'r--', lw=2, label="Line B→C")
plt.plot([C[0], D[0]], [C[1], D[1]], 'r--', lw=2, label="Line C→D")

# Mark special points
for p, labelp in zip([A, B, C, D], ["A", "B", "C", "D"]):
    plt.scatter(p[0], p[1], color='red', s=80, zorder=5)
    plt.text(p[0], p[1], labelp, color='red', fontsize=12)

# Optionally highlight the curve from x=0.045..2.65 in green
plt.plot(x_curve, y_curve, 'g-', lw=2, label="Curve x=0.045..2.65")

# Annotate the area on the plot
plt.text(1.2, 10, f"Area = {area:.3f} kN·mm", color='purple', fontsize=12)

plt.xlabel("Deflection (mm)")
plt.ylabel("Load (kN)")
plt.title("Polygon: A→B→C→D + curve (2.65→0.045) → A")
plt.grid(True)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.show()
