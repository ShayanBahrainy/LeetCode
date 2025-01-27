class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        IncomingGraph = [[] for _ in range(numCourses)]
        for preq in prerequisites: 
            IncomingGraph[preq[1]].append(preq[0])
        PrerequisiteMap = [set() for _ in range(numCourses)]
        for course in range(numCourses):
            queue = deque([course])
            visited = set()
            while queue:
                c = queue.popleft()
                prereq = IncomingGraph[c]
                for pre in prereq:
                    if pre in visited:
                        continue
                    PrerequisiteMap[course].add(pre)
                    queue.append(pre)
                    visited.add(pre)
        ans = [False] * len(queries)
        for i in range(len(queries)):
            query = queries[i]
            if query[0] in PrerequisiteMap[query[1]]:
                ans[i] = True
        return ans



                
