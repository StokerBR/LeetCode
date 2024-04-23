class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        nodes = n

        if nodes == 1:
            return [0]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        leaf_nodes = []
        for node in graph.keys():
            if len(graph[node]) == 1:
                leaf_nodes.append(node)

        while nodes > 2:
            nodes -= len(leaf_nodes)

            leaf_nodes_next = []

            for leaf in leaf_nodes:
                adjacent = graph[leaf].pop()
                graph[adjacent].remove(leaf)

                if len(graph[adjacent]) == 1:
                    leaf_nodes_next.append(adjacent)
            
            leaf_nodes = leaf_nodes_next

        return leaf_nodes