class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        h={i:[] for i in range(numCourses)}
        for p in prerequisites:
            h[p[0]].append(p[1])
        visited=set()
        studied=set()
        def dfs(course):
            if course in studied:
                return True
            visited.add(course)
            for c in h[course]:
                if c in visited or not dfs(c):
                    return False
            visited.remove(course)
            studied.add(course)
            return True
        for c in h:
            if not dfs(c):
                return False
        return True

        