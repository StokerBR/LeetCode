class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for v1, v2, w in times:
            edges[v1].append((v2, w))

        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
                
            visited.add(node)
            t = max(t, weight)

            for adjacent_node, weight2 in edges[node]:
                if adjacent_node not in visited:
                    heapq.heappush(minHeap, (weight + weight2, adjacent_node))
        
        return t if len(visited) == n else -1