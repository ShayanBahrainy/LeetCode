class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n) ]
        parent = [-1] * n
        depth = [0] * n

        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
            self._union(edge[0] - 1, edge[1] - 1, parent, depth)
        
        num_of_groups_for_component = {}

        for node in range(n):
            number_of_groups = self._get_number_of_groups(adj_list, node, n)
            if number_of_groups == -1:
                return -1
            root_node = self._find(node, parent)
            num_of_groups_for_component[root_node] = max(num_of_groups_for_component.get(root_node, 0),number_of_groups)
        total_number_of_groups = sum(num_of_groups_for_component.values())
        return total_number_of_groups
    def _get_number_of_groups(self, adj_list, src_node, n):
        nodes_queue = deque()
        layer_seen = [-1] * n
        nodes_queue.append(src_node)
        layer_seen[src_node] = 0
        deepest_layer = 0

        while nodes_queue:
            num_of_nodes_in_layer = len(nodes_queue)
            for _ in range(num_of_nodes_in_layer):
                current_node = nodes_queue.popleft()
                for neighbor in adj_list[current_node]:
                    if layer_seen[neighbor] == -1:
                        layer_seen[neighbor] = deepest_layer + 1
                        nodes_queue.append(neighbor)
                    else:
                        if layer_seen[neighbor] == deepest_layer:
                            return -1
            deepest_layer += 1
        return deepest_layer
    def _find(self, node, parent):
        while parent[node] != -1:
            node = parent[node]
        return node
    def _union(self, node1, node2, parent, depth):
        node1 = self._find(node1, parent)
        node2 = self._find(node2, parent)

        if node1 == node2:
            return
        if depth[node1] < depth[node2]:
            node1, node2 = node2, node1
        parent[node2] = node1
        if depth[node1] == depth[node2]:
            depth[node1] += 1