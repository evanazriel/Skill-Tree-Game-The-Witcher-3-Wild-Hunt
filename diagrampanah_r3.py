import matplotlib.pyplot as plt
import networkx as nx

# Inisialisasi Objek Graf Berarah (DiGraph)
G = nx.DiGraph()

# Mendefinisikan Himpunan A (Skills) dan Himpunan B (Kategori)
set_A = ["a1: Muscle Mem", "a2: Prec Blows", "a3: Resolve", "a4: Act Shield", "a5: Metab Ctrl", "a6: Acq Tol"]
set_B = ["b1: Combat", "b2: Signs", "b3: Alchemy", "b4: General"]

G.add_nodes_from(set_A, bipartite=0)
G.add_nodes_from(set_B, bipartite=1)

# Mendefinisikan Sisi Pemetaan (Edges R3 dari A ke B)
edges_R3 = [
    ("a1: Muscle Mem", "b1: Combat"),
    ("a2: Prec Blows", "b1: Combat"),
    ("a3: Resolve", "b1: Combat"),
    ("a4: Act Shield", "b2: Signs"),
    ("a5: Metab Ctrl", "b3: Alchemy"),
    ("a6: Acq Tol", "b3: Alchemy")
]
G.add_edges_from(edges_R3)

# Mengatur Tata Letak Bipartit (Kolom Kiri untuk A, Kolom Kanan untuk B)
pos = {}
# Atur posisi sumbu X dan Y untuk Himpunan A (Kiri, x=0)
for i, node in enumerate(set_A):
    pos[node] = (0, 5 - i)
# Atur posisi sumbu X dan Y untuk Himpunan B (Kanan, x=2)
for i, node in enumerate(set_B):
    pos[node] = (2, 3.5 - i)

# Konfigurasi Tampilan Gambar (Figure Size)
plt.figure(figsize=(9, 6))

# Menggambar Simpul dengan Warna Berbeda untuk Himpunan A dan B
nx.draw_networkx_nodes(G, pos, nodelist=set_A, node_size=1000, node_color="skyblue", edgecolors="black")
nx.draw_networkx_nodes(G, pos, nodelist=set_B, node_size=1000, node_color="lightgreen", edgecolors="black")

# Menggambar Garis Panah Penghubung (Edges)
nx.draw_networkx_edges(G, pos, edge_color="gray", width=2, arrowstyle="->", arrowsize=15)

# Menambahkan Label Teks pada Simpul
nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold", font_color="black")

plt.title("Diagram Panah Pemetaan Relasi R3 (Himpunan A ke B) - The Witcher 3", fontsize=11, fontweight="bold", pad=20)
plt.axis("off")

plt.savefig("diagram_panah_r3.png", format="png", dpi=300, bbox_inches="tight")
plt.show()