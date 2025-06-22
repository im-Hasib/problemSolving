from collections import deque


def bfs(tree,start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            print(node, end=" ")

            for neighbor in tree[node]:
                queue.append(neighbor)


tree = {
    'A': ['B', 'C'],  # Node A connects to B and C
    'B': ['D', 'E'],  # Node B connects to D and E
    'C': ['F', 'G'],  # Node C connects to F and G
    'D': ['H', 'I'],  # Node D connects to H and I
    'E': ['J', 'K'],  # Node E connects to J and K
    'F': ['L', 'M'],  # Node F connects to L and M
    'G': ['N', 'O'],  # Node G connects to N and O
    'H': [], 'I': [], 'J': [], 'K': [],  # Leaf nodes have no children
    'L': [], 'M': [], 'N': [], 'O': []   # Leaf nodes have no children
}
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']  # cycle: A -> B -> C -> A
}
bfs(graph, 'A')

