from collections import deque


# Function to perform BFS
def bfs(graph, start):
    visited = {node: False for node in graph}
    distance = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    visited[start] = True
    distance[start] = 0

    queue = deque([start])
    order_of_traversal = []

    while queue:
        current = queue.popleft()
        order_of_traversal.append(current)

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)

    return order_of_traversal, distance


# Function to perform DFS
def dfs(graph):
    visited = {node: False for node in graph}
    parent = {node: None for node in graph}
    discovery_time = {}
    finish_time = {}
    time_counter = [0]  # Using list to allow modification inside inner function

    def explore(node):
        visited[node] = True
        time_counter[0] += 1
        discovery_time[node] = time_counter[0]

        for neighbor in graph[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                explore(neighbor)

        time_counter[0] += 1
        finish_time[node] = time_counter[0]

    for vertex in graph:
        if not visited[vertex]:
            explore(vertex)

    return discovery_time, finish_time


# Function to input the graph
def input_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    print("Enter the adjacency list for each node (format: node neighbor1 neighbor2 ...):")
    for _ in range(num_nodes):
        input_data = input().strip().split()
        node = input_data[0]
        neighbors = input_data[1:]
        graph[node] = neighbors

    return graph


# Main menu-driven function
def main():
    graph = input_graph()

    while True:
        print("\nMenu:")
        print("1. Run BFS")
        print("2. Run DFS")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            start_node = input("Enter the starting node for BFS: ")
            bfs_order, bfs_distance = bfs(graph, start_node)
            print("\nBFS Order of Traversal:", bfs_order)
            print("BFS Distances from starting node:", bfs_distance)

        elif choice == '2':
            dfs_discovery, dfs_finish = dfs(graph)
            print("\nDFS Discovery Times:", dfs_discovery)
            print("DFS Finish Times:", dfs_finish)

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select again.")


# Execute the program
if __name__ == "__main__":
    main()
