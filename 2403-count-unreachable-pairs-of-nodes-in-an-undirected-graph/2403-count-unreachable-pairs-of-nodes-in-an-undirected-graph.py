class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        sizes = [0] * n
        for i in range(n):
            if not visited[i]:
                sizes[i] = self.dfs(i, graph, visited)

        ans = 0
        for i in range(n):
            ans+= sizes[i] * (n-sizes[i])

        return ans//2

    def dfs(self, u: int, graph, visited) -> int:
        visited[u] = True
        size = 1
        for v in graph[u]:
            if not visited[v]:
                size += self.dfs(v, graph, visited)
        return size
