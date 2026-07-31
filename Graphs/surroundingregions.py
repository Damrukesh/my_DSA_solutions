class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        from collections import deque
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        visited=set()
        def markt(c,d):
            q=deque()
            q.append((c,d))
            visited.add((c,d))
            while q:
                c,d=q.popleft()
                for a,b in directions:
                    row=c+a
                    col=d+b
                    if row in range(m) and col in range(n) and board[row][col]=="O" and (row,col) not in visited:
                        q.append((row,col))
                        visited.add((row,col))
                        board[row][col]="t"
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and board[i][j]=="O":
                    board[i][j]="t"
                    markt(i,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="t":
                    board[i][j]="O"

            
                
