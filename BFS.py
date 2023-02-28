import collections
import numpy as np
import networkx as nx


def bfs(graph, root):

    visited = set()
    searchlist = collections.deque([root])
    visited.add(root)

    while searchlist:

        # pop the left most node from the list and return this value
        leftmost = searchlist.popleft()
        print(str(leftmost) + " ", end ="")

        # search the neighbor of the leftmost node, if the neighbor is not visited, add it to the visited list
        # also add it to the searchlist for future search.
        for item in graph[leftmost]:
            if item not in visited:
                visited.add(item)
                searchlist.append(item)



# create a random graph based on the number of vertices(vertices) and how each verticies can be connected
# connectivity of graph can range from 0 to 9, from highest,(every nodes are connected) to 9 (least connected.)
def random_graph(vertices, connectivity):
    arr = np.random.randint(0, 10, (vertices, vertices))
    sym = (arr + arr.T)

    np.fill_diagonal(sym, 0)

    mat = (sym > connectivity).astype(int)

    G = {k: [i for i, j in enumerate(v) if j == 1] for k, v in enumerate(mat)}
    return G