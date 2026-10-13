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

# VISUALISASI 1: DIAGRAM HASSE (UNTUK URUTAN PARSIAL R1) 
G_poset = nx.DiGraph()
G_poset.add_nodes_from(nodes)
G_poset.add_edges_from(edges_r1)

plt.figure(figsize=(6, 5))
# Menggunakan shell_layout atau planar_layout agar struktur hierarki terlihat seperti Diagram Hasse
pos_hasse = {
    "a1": (0, 2),
    "a2": (-1, 1),
    "a3": (1, 1),
    "a4": (2, 2),
    "a5": (-1, -1),
    "a6": (1, -1),
}

nx.draw_networkx_nodes(
    G_poset, pos_hasse, node_size=700, node_color="orange", edgecolors="black"
)
nx.draw_networkx_edges(
    G_poset,
    pos_hasse,
    edge_color="black",
    width=2,
    arrowstyle="->",
    arrowsize=15,
)
nx.draw_networkx_labels(
    G_poset, pos_hasse, font_size=11, font_weight="bold", font_color="black"
)

plt.title(
    "Diagram Hasse / Urutan Parsial R1 (Prasyarat Skill)",
    fontsize=11,
    fontweight="bold",
)
plt.axis("off")
plt.savefig("diagram_hasse_r1.png", format="png", dpi=300, bbox_inches="tight")
plt.show()
