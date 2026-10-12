import matplotlib.pyplot as plt
import networkx as nx

#Inisialisasi Objek Graf Berarah (Directed Graph / DiGraph)
G = nx.DiGraph()


#Mendefinisikan Himpunan Simpul (Nodes) / Kemampuan (Skills) A
nodes = ["a1", "a2", "a3", "a4", "a5", "a6"]
G.add_nodes_from(nodes)

#Mendefinisikan Sisi Berarah (Edges) beserta Keterangan/Bobotnya
edges_with_labels = [
    ("a1", "a2", {"label": "se-cabang"}),
    ("a2", "a1", {"label": "se-cabang"}),
    ("a1", "a3", {"label": "se-cabang"}),
    ("a3", "a1", {"label": "se-cabang"}),
    ("a2", "a3", {"label": "se-cabang"}),
    ("a3", "a2", {"label": "se-cabang"}),
    ("a5", "a6", {"label": "se-cabang"}),
    ("a6", "a5", {"label": "se-cabang"})
]
G.add_edges_from(edges_with_labels)

#Mengatur Tata Letak (Layout) Simpul
pos = nx.circular_layout(G)

#Konfigurasi Tampilan Gambar (Figure Size)
plt.figure(figsize=(7, 7))

#Menggambar Komponen Graf dengan Kurva Melengkung (arc3) agar garis dua arah tidak bertumpuk
nx.draw_networkx_nodes(G, pos, node_size=800, node_color="lightgreen", edgecolors="black")
nx.draw_networkx_edges(G, pos, edge_color="darkgreen", width=2, arrowstyle="->", arrowsize=15, connectionstyle="arc3,rad=0.2")
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold", font_color="black")

#Menambahkan Label Teks di Atas Garis (Edge Labels)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color="darkblue")

plt.title("Graf Berarah Relasi Satu Cabang (R2) - The Witcher 3", fontsize=12, fontweight="bold", pad=20)
plt.axis("off")


plt.savefig("graf_r2_witcher3.png", format="png", dpi=300, bbox_inches="tight")

plt.show()
