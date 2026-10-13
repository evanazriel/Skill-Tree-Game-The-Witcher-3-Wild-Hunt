import matplotlib.pyplot as plt
import networkx as nx

# 1. Inisialisasi Graf Berarah R1
G_r1 = nx.DiGraph()
nodes = ["a1", "a2", "a3", "a4", "a5", "a6"]
G_r1.add_nodes_from(nodes)
edges_r1 = [("a1", "a2"), ("a1", "a3"), ("a2", "a3"), ("a5", "a6")]
G_r1.add_edges_from(edges_r1)

# 2. Hitung Transitive Closure
tc_graph = nx.transitive_closure(G_r1)

pos = nx.spring_layout(tc_graph, seed=42)

# 4. Gambar Graf
plt.figure(figsize=(6, 6))
nx.draw_networkx_nodes(tc_graph, pos, node_size=700, node_color="skyblue", edgecolors="black")
nx.draw_networkx_edges(tc_graph, pos, edge_color="navy", width=1.5, arrowstyle="->", arrowsize=15, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_labels(tc_graph, pos, font_size=11, font_weight="bold")

plt.title("Transitive Closure (R1*) - Gaya Natural", fontsize=11, fontweight="bold")
plt.axis("off")
plt.show()