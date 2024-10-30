from collections import deque

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Depth-First Search (DFS) using recursion
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()  # Initialize the visited set on the first call
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)  # Mark the node as visited
        for neighbor in graph[node]:  # Visit all neighbors
            dfs_recursive(graph, neighbor, visited)

# Depth-First Search (DFS) using a stack
def dfs_stack(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    stack = [start_node]  # Stack initialized with the start node

    while stack:
        node = stack.pop()  # Pop the last node added
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark as visited
            stack.extend(reversed(graph[node]))  # Add neighbors to the stack in reverse order

# Breadth-First Search (BFS) using a queue
def bfs(graph, start_node):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start_node])  # Queue initialized with the start node

    while queue:
        node = queue.popleft()  # Dequeue the first node
        if node not in visited:
            print(node, end=" ")  # Process the node
            visited.add(node)  # Mark as visited
            queue.extend(graph[node])  # Enqueue all neighbors

# Test DFS and BFS
print("Depth-First Search (DFS) - Recursive:")
dfs_recursive(graph, 'A')
print("\nDepth-First Search (DFS) - Stack:")
dfs_stack(graph, 'A')
print("\nBreadth-First Search (BFS):")
bfs(graph, 'A')
