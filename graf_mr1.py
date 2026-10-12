import matplotlib.pyplot as plt
import networkx as nx

# Inisialisasi Objek Graf Berarah (Directed Graph / DiGraph)
G = nx.DiGraph()

# Mendefinisikan Himpunan Simpul (Nodes) / Kemampuan (Skills) A
nodes = ["a1", "a2", "a3", "a4", "a5", "a6"]
G.add_nodes_from(nodes)

# Mendefinisikan Sisi Berarah (Edges) beserta Keterangan/Bobotnya
edges_with_labels = [
    ("a1", "a2", {"label": "prasyarat"}),
    ("a1", "a3", {"label": "prasyarat"}),
    ("a2", "a3", {"label": "prasyarat"}),
    ("a5", "a6", {"label": "prasyarat"})
]
G.add_edges_from(edges_with_labels)

# Mengatur Tata Letak (Layout) Simpul
pos = nx.circular_layout(G)

# Konfigurasi Tampilan Gambar (Figure Size)
plt.figure(figsize=(7, 7))

# Menggambar Komponen Graf (Simpul, Tepi, dan Label Simpul)
nx.draw_networkx_nodes(G, pos, node_size=800, node_color="skyblue", edgecolors="black")
nx.draw_networkx_edges(G, pos, edge_color="teal", width=2, arrowstyle="->", arrowsize=20, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold", font_color="black")

# Menambahkan Label Teks di Atas Garis (Edge Labels)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9, font_color="darkred")

# Pengaturan Judul dan Visual Akhir
plt.title("Graf Berarah Relasi Prasyarat Skill (R1) - The Witcher 3", fontsize=12, fontweight="bold", pad=20)
plt.axis("off")

plt.savefig("graf_r1_witcher3.png", format="png", dpi=300, bbox_inches="tight")

plt.show()