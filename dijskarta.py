import heapq

def dijkstra(graph, source):
    # Number of vertices in the graph
    n = len(graph)

    # Distance array to store the shortest distance from the source
    distances = [float('inf')] * n
    distances[source] = 0

    # Priority queue to process vertices in increasing order of distance
    priority_queue = [(0, source)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip processing if the distance is already larger
        if current_distance > distances[current_vertex]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage
if __name__ == "__main__":
    # Graph representation as an adjacency list
    # Each index represents a vertex, and it contains a list of (neighbor, weight)
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: []
    }

    source = 0
    shortest_distances = dijkstra(graph, source)

    print("Vertex\tDistance from Source")
    for vertex, distance in enumerate(shortest_distances):
        print(f"{vertex}\t{distance}")
