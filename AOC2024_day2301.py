import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = set()

with open("AOC2024_day23.txt") as finpt:
    for inpt in finpt:

        left, right = inpt.strip().split("-")
        G.add_node(left)
        G.add_node(right)
        G.add_edge(left,right)
        nodes.add(left)
        nodes.add(right)

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

a = nx.triangles(G)
print(a)

totalnum = 0
for t in a:
    if 't' in t:
        totalnum += a[t]

print(totalnum)