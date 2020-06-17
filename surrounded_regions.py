'''
Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

'''



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        if m==0:
            return
        n = len(board[0])
        if n==0:
            return
        queue = collections.deque([])
        for i in range(m):
            if board[i][0] == "O":
                board[i][0] = "1"
                queue.append((i-1, 0)); queue.append((i+1, 0))
                queue.append((i, 1))

            if board[i][n-1] == "O":
                board[i][n-1] = "1" 
                queue.append((i-1, n-1)); queue.append((i+1, n-1))
                queue.append((i, n-2))
        
        
        for i in range(n):
            if board[0][i] == "O":
                board[0][i] = "1"
                queue.append((0, i-1)); queue.append((0, i+1))      
                queue.append((1, i))
                
            if board[m-1][i] == "O":
                board[m-1][i] = "1"
                queue.append((m-1, i-1)); queue.append((m-1, i+1))
                queue.append((m-2, i));     
                
                
        print(queue)

        while queue:
            r, c = queue.popleft()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "1"
                queue.append((r-1, c)); queue.append((r+1, c))
                queue.append((r, c-1)); queue.append((r, c+1))
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "1":
                    board[i][j] ="O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
                else:
                    continue
        
