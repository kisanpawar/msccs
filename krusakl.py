# Class to represent a graph edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Number of vertices
        self.edges = []  # List to store graph edges

    def add_edge(self, src, dest, weight):
        self.edges.append(Edge(src, dest, weight))

    # Find the subset of an element (with path compression)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union of two subsets by rank
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Kruskal's algorithm to find MST
    def kruskal_mst(self):
        # Sort edges by weight
        self.edges.sort(key=lambda edge: edge.weight)

        parent = []
        rank = []
        mst = []

        # Initialize parent and rank
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        # Number of edges in MST is (vertices - 1)
        e = 0
        i = 0

        while e < self.vertices - 1:
            # Pick the smallest edge
            edge = self.edges[i]
            i += 1

            # Find roots of the source and destination
            x = self.find(parent, edge.src)
            y = self.find(parent, edge.dest)

            # If no cycle is formed, add the edge to MST
            if x != y:
                mst.append(edge)
                self.union(parent, rank, x, y)
                e += 1

        # Print the MST
        print("Edges in the Minimum Spanning Tree:")
        for edge in mst:
            print(f"{edge.src} -- {edge.dest} == {edge.weight}")

# Example usage
if __name__ == "__main__":
    # Create a graph with 4 vertices
    graph = Graph(4)
    graph.add_edge(0, 1, 10)
    graph.add_edge(0, 2, 6)
    graph.add_edge(0, 3, 5)
    graph.add_edge(1, 3, 15)
    graph.add_edge(2, 3, 4)

    # Find and print the MST
    graph.kruskal_mst()
