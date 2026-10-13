import matplotlib.pyplot as plt
import networkx as nx

# 1. Inisialisasi Data
nodes = ["a1", "a2", "a3", "a4", "a5", "a6"]

# Relasi R1 (Prasyarat - Kandidat Urutan Parsial / Poset)
edges_r1 = [("a1", "a2"), ("a1", "a3"), ("a2", "a3"), ("a5", "a6")]

# Relasi R2 (Kesetaraan Kategori / Ekuivalensi)
edges_r2 = [
    ("a1", "a1"),
    ("a2", "a2"),
    ("a3", "a3"),
    ("a4", "a4"),
    ("a5", "a5"),
    ("a6", "a6"),
    ("a1", "a2"),
    ("a2", "a1"),
    ("a1", "a3"),
    ("a3", "a1"),
    ("a2", "a3"),
    ("a3", "a2"),
    ("a5", "a6"),
    ("a6", "a5"),
]

G_eq = nx.Graph()
G_eq.add_nodes_from(nodes)
# Masukkan sisi selain loop diri sendiri untuk digambar
G_eq.add_edges_from([(u, v) for u, v in edges_r2 if u != v])

plt.figure(figsize=(6, 5))
pos_eq = nx.spring_layout(G_eq, seed=42)

nx.draw_networkx_nodes(
    G_eq, pos_eq, node_size=700, node_color="skyblue", edgecolors="black"
)
nx.draw_networkx_edges(G_eq, pos_eq, edge_color="blue", width=1.5, style="dashed")
nx.draw_networkx_labels(
    G_eq, pos_eq, font_size=11, font_weight="bold", font_color="black"
)

plt.title(
    "Kelas Ekuivalensi R2 (Pengelompokan Kategori)",
    fontsize=11,
    fontweight="bold",
)
plt.axis("off")
plt.savefig("kelas_ekuivalensi_r2.png", format="png", dpi=300, bbox_inches="tight")
plt.show()
