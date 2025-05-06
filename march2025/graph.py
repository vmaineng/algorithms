matrix = [
    [0, 1, 1, 0],  # Node 0
    [1, 0, 1, 0],  # Node 1
    [1, 1, 0, 1],  # Node 2
    [0, 0, 1, 0]   # Node 3
]

node_values = [5, 3, 7, 2] #arbitary values
#              0  1  2  3
# Print node values
print("Node values:")
for i in range(len(matrix)):
    print(f"Node {i}: {node_values[i]}")

# Print connections
print("\nConnections:")
for i in range(len(matrix)):
    connections = [j for j in range(len(matrix[i])) if matrix[i][j] == 1]
    print(f"Node {i} connects to: {connections}")