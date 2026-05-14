class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        R=len(image)
        C=len(image[0])
        from collections import deque
        q=deque()
        q.append((sr,sc))
        start=image[sr][sc]
        image[sr][sc]=color
        if start==color:
            return image
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                image[r][c]=color
                for a,b in directions:
                    row=a+r
                    col=b+c
                    if row in range(R) and col in range(C) and image[row][col]==start:
                        q.append((row,col))
                        image[row][col]=color
        return image                



# time complexity is O(m*n) where m and n are the number of rows and columns in the grid
# space complexity is O(m*n) in the worst case when all pixels are the same color and we have to add all of them to the queue.
# traverse the grid once to find the starting pixel and then use bfs to change the color of the connected pixels with the same color. Use a queue to keep track of the pixels to be processed and mark the visited pixels by changing their color to the new color.