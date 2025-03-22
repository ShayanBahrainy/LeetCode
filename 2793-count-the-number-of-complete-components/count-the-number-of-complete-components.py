class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = DefaultDict(set)
        count = 0
        for edge in edges:
            connections[edge[0]].add(edge[1])
            connections[edge[1]].add(edge[0])
        count += n - len(connections)
        starting = connections.keys()
        seen = set()
        components = []
        for startnode in starting:
            if startnode in seen:
                continue
            queue = deque()
            component = []
            queue.appendleft(startnode)
            while queue:
                current = queue.pop()
                for node in connections[current]:
                    if node not in seen:
                        seen.add(node)
                        queue.appendleft(node)
                        component.append(node)
            components.append(component)
        for component in components:
            parts = set(component)
            allConnected = True
            for node in parts:
                parts.remove(node)
                if not parts == connections[node]:
                    allConnected = False
                    break
                parts.add(node)
            if allConnected:
                count += 1
        return count
            
    def runDFS(self,): pass