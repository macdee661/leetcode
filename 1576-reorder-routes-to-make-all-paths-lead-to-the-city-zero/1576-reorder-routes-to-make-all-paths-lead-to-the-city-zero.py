from collections import deque, defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        graph = {}
        queue = deque([0])

        graph = defaultdict(list)
        
        for u, v in connections:
            graph[u].append((v, True)) 
            graph[v].append((u, False))
        count = 0
        while queue:
            node = queue.popleft()
            visited.add(node)
            for neighbor, needs_reverse in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    if needs_reverse:
                        count += 1
        return count