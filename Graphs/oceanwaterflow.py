class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R=len(heights)
        C=len(heights[0])
        ans=[]
        from collections import deque
        pacific,atlantic=set(),set()
        aq=deque()
        pq=deque()
        for i in range(len(heights[0])):
            pacific.add((0,i))
            atlantic.add((R-1,i))
            pq.append((0,i))
            aq.append((R-1,i))
        for i in range(len(heights)):
            pacific.add((i,0))
            atlantic.add((i,C-1))
            pq.append((i,0))
            aq.append((i,C-1))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]


        while pq:
            a,b=pq.popleft()
            for c,d in directions:
                row=a+c
                col=b+d
                if row in range(R) and col in range(C) and (row,col) not in pacific and heights[row][col]>=heights[a][b]:
                    pacific.add((row,col))
                    pq.append((row,col))
        while aq:
            a,b=aq.popleft()
            for c,d in directions:
                row=a+c
                col=b+d
                if row in range(R) and col in range(C) and (row,col) not in atlantic and heights[row][col]>=heights[a][b]:
                    atlantic.add((row,col))
                    aq.append((row,col))

        for a,b in pacific:
            if (a,b) in atlantic:
                ans.append([a,b])
        return ans

                    
                        

        
        
        