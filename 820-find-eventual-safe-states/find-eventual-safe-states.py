class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        terminalNodes = []
        linkFrom = {}
        safeNodes = set()
        ProcessQueue = []
        for i in range(len(graph)):
            if len(graph[i]) == 0:
                terminalNodes.append(i)
            for node in graph[i]:
                linkFrom[node] = linkFrom.get(node, []) + [i]
        ProcessQueue += terminalNodes
        newsafes = 1
        while newsafes > 0:
            newsafes = 0
            index = 0
            while index < len(ProcessQueue):
                node = ProcessQueue[index]
                if not linkFrom.__contains__(node):
                    ProcessQueue.pop(index)
                    continue
                isallsafe = False
                for originNode in linkFrom[node]:
                    if originNode == node:
                        continue
                    if originNode in safeNodes:
                        continue
                    safeness = self.isSafe(originNode, graph, safeNodes, terminalNodes)
                    if safeness:
                        newsafes += 1
                        safeNodes.add(originNode)
                        ProcessQueue.append(originNode)
                    else:
                        isallsafe = False
                if isallsafe:
                    ProcessQueue.pop(index)
                index += 1
        result = list(safeNodes) + terminalNodes
        result.sort()
        return result
    def isSafe(self, originNode, graph, safeNodes, terminalNodes):
        for destinationNode in graph[originNode]:
            if destinationNode in safeNodes:
                continue
            if destinationNode in terminalNodes:
                continue
            return False
        return True
            