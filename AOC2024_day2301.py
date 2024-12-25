import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

tnodes = set()

with open("AOC2024_day23.txt") as finpt:
    for inpt in finpt:

        left, right = inpt.strip().split("-")
        G.add_node(left)
        G.add_node(right)
        G.add_edge(left,right)
        if 't' in left:
            tnodes.add(left)
        if 't' in right:
            tnodes.add(right)

# nx.draw(G, with_labels=True, font_weight='bold')
# plt.show()

all_cliques= nx.enumerate_all_cliques(G)
triad_cliques=[x for x in all_cliques if len(x)==3 ]

# print(triad_cliques)
totalnum = 0
for tc in triad_cliques:
    for n in tc:
        if n[0] == 't':
            totalnum += 1
            break

print(totalnum)