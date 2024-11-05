import sys
from collections import deque

# Class for Graph used in Kruskal's Algorithm
class KruskalGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal_mst(self):
        result = []
        self.graph.sort(key=lambda x: x[2])  # Sort edges by weight
        parent = list(range(self.V))
        rank = [0] * self.V

        for u, v, w in self.graph:
            x, y = self.find(parent, u), self.find(parent, v)
            if x != y:  # Check for cycle
                result.append((u, v, w))
                self.union(parent, rank, x, y)

        print("\nKruskal's Algorithm Result (Edge - Weight):")
        for u, v, weight in result:
            print(f"{u} - {v}    {weight}")

# Class for Graph used in Prim's Algorithm
class PrimGraph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]  # Adjacency matrix

    def printMST(self, parent):
        """Print the edges of the Minimum Spanning Tree."""
        print("\nPrim's Algorithm Result (Edge - Weight):")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i} \t {self.graph[i][parent[i]]}")

    def primMST(self):
        """Implement Prim's algorithm to find the MST."""
        key = [sys.maxsize] * self.V  # Initialize all keys as infinite
        parent = [-1] * self.V  # Array to store constructed MST
        key[0] = 0  # Start from the first vertex
        mstSet = [False] * self.V  # Track vertices included in the MST

        for _ in range(self.V):
            # Select the minimum key vertex not yet included in the MST
            u = min((key[i], i) for i in range(self.V) if not mstSet[i])[1]
            mstSet[u] = True  # Include the selected vertex in the MST

            # Update the key and parent for adjacent vertices
            for v in range(self.V):
                if self.graph[u][v] and not mstSet[v] and key[v] > self.graph[u][v]:
                    key[v], parent[v] = self.graph[u][v], u

        self.printMST(parent)  # Print the result

# Function to input the graph for Kruskal's Algorithm
def input_kruskal_graph():
    vertices = int(input("\nEnter the number of vertices for Kruskal's Algorithm: "))
    g = KruskalGraph(vertices)

    print("Enter the adjacency matrix for Kruskal's Algorithm (row by row):")
    for i in range(vertices):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        for j in range(i + 1, vertices):
            if row[j] != 0:
                g.add_edge(i, j, row[j])

    g.kruskal_mst()

# Function to input the graph for Prim's Algorithm
def input_prim_graph():
    vertices = int(input("\nEnter the number of vertices for Prim's Algorithm: "))
    g = PrimGraph(vertices)

    print("Enter the adjacency matrix for Prim's Algorithm (row by row):")
    for i in range(vertices):
        g.graph[i] = list(map(int, input(f"Row {i + 1}: ").split()))

    g.primMST()  # Compute and display the MST

# Main menu-driven function
def main():
    while True:
        print("\nMenu:")
        print("1. Run Kruskal's Algorithm")
        print("2. Run Prim's Algorithm")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            input_kruskal_graph()

        elif choice == '2':
            input_prim_graph()

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select again.")

# Execute the program
if __name__ == "__main__":
    main()
