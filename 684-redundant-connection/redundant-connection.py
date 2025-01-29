class Solution:
    cycle_start = -1
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        N = len(edges)

        visited = [False] * N

        parent = [-1] * N

        adjList = [[] for _ in range(N)]

        for edge in edges:
            u = edge[0]
            v = edge[1]
            adjList[u - 1].append(v - 1)
            adjList[v - 1].append(u - 1)
        self._dfs(0, visited, adjList, parent)
        cycle_nodes = {}
        node = self.cycle_start
        while True:
            cycle_nodes[node] = 1
            node = parent[node]
            if node == self.cycle_start:
                break
        for i in range(len(edges) -1, -1, -1):
            if (edges[i][0] - 1) in cycle_nodes and (edges[i][1] - 1) in cycle_nodes:
                return edges[i]
    def _dfs(self, node, visited, adjList, parent):
        visited[node] = True
        for adj in adjList[node]:
            if not visited[adj]:
                parent[adj] = node
                self._dfs(adj, visited, adjList, parent)
            elif adj != parent[node] and self.cycle_start == -1:
                self.cycle_start = adj
                parent[adj] = node