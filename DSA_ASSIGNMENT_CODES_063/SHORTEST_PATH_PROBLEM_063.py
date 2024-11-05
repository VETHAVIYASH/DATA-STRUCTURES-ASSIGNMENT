import heapq


# Dijkstra's Algorithm
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Topological Sort Helper for DAG
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]


# Dynamic Programming for Shortest Paths in Acyclic Graphs
def shortest_path_dag(graph, start):
    topological_order = topological_sort(graph)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for node in topological_order:
        if distances[node] != float('inf'):
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


# Floyd-Warshall Algorithm
def floyd_warshall(graph):
    num_vertices = len(graph)
    distance = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    for u in range(num_vertices):
        distance[u][u] = 0
        for v, w in graph[u].items():
            distance[u][v] = w

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance


# Function to input the graph from the user
def input_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))
    for i in range(vertices):
        edges = input(f"Enter the edges for vertex {i} (format: neighbor1:weight neighbor2:weight ...): ")
        graph[i] = {}
        for edge in edges.split():
            neighbor, weight = edge.split(':')
            graph[i][int(neighbor)] = int(weight)
    return graph


# Main function to run the menu
def main():
    while True:
        print("\nMenu:")
        print("1. Dijkstra's Algorithm")
        print("2. Shortest Path in Acyclic Graph (Dynamic Programming)")
        print("3. Floyd-Warshall Algorithm")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '4':
            break

        graph = input_graph()

        if choice == '1':
            start = int(input("Enter the start vertex: "))
            distances = dijkstra(graph, start)
            print("\nShortest distances from vertex", start, ":", distances)

        elif choice == '2':
            start = int(input("Enter the start vertex: "))
            distances = shortest_path_dag(graph, start)
            print("\nShortest distances from vertex", start, ":", distances)

        elif choice == '3':
            distances = floyd_warshall(graph)
            print("\nDistance matrix:")
            for row in distances:
                print(row)

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
