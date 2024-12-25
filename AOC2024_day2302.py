import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

with open("AOC2024_day23.txt") as finpt:
    for inpt in finpt:

        left, right = inpt.strip().split("-")
        G.add_node(left)
        G.add_node(right)
        G.add_edge(left,right)

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

# Find all maximal cliques
cliques = list(nx.find_cliques(G))

# Identify the largest clique
largest_clique = max(cliques, key=len)

# Print the largest clique
print("Largest clique:", ','.join(sorted(largest_clique)))
print("Size of the largest clique:", len(largest_clique))