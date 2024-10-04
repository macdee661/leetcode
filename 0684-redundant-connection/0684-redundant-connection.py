class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Helper function to find the root parent of a node
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        # Helper function to union two nodes
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
            else:
                return False
            return True
        
        # Initialize the parent array
        parent = list(range(len(edges) + 1))
        
        # Iterate through each edge
        for x, y in edges:
            if not union(x, y):  # If x and y are already connected, it's the redundant connection
                return [x, y]
