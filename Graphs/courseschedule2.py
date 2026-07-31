class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        h={i:[] for i in range(numCourses)}
        for p in prerequisites:
            h[p[0]].append(p[1])
        path=set()
        canstudy=set()
        self.ans=[]
        def study(root):
            if root in canstudy:
                return True
            path.add(root)
            for s in h[root]:
                if s in path or not study(s):
                    return False
            path.remove(root)
            canstudy.add(root)
            self.ans.append(root)
            return True
        for c in h:
            if not study(c):
                return []
        return self.ans




        