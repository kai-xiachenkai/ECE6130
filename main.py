from BFS import *
from matplotlib import pyplot as plt

G = random_graph(7, 9)
print("Following is the generated graph: ")
print(G)
print("Following is Breadth First Traversal: ")
bfs(G, 0)

g = nx.Graph(G)
nx.draw(g,with_labels = True)
plt.show()

