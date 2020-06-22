'''

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	    -10	1
10	    30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.



'''


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        m = len(dungeon)
        n = len(dungeon[0])
        
        def check(i,j):
            if 0<=i<m and 0<=j<n:
                return True
            else:
                return False
        
        
        res = 1
        
        
        bd = [[-1 for i in range(n)] for j in range(m)]
        
        
        def getMin(i,j):
            mini = 10**7
            if check(i+1,j):
                if bd[i+1][j]<mini:
                    mini = bd[i+1][j]
            if check(i,j+1):
                if bd[i][j+1]<mini:
                    mini = bd[i][j+1]
            return mini
                
            
        
        que = []
        i = m-1
        j = n-1
        
        res= res - dungeon[i][j]
        if res<=0:
            res=1
                
        bd[i][j] = res
        if check(i-1,j):
            que.append((i-1,j))
        if check(i,j-1):
            que.append((i,j-1))

        while que:
            
            i,j = que.pop(0)
            
            if bd[i][j] ==-1:
                
                res = getMin(i,j)
                
                
                res= res - dungeon[i][j]
                if res<=0:
                    res=1
                bd[i][j] = res
                if check(i-1,j):
                    que.append((i-1,j))
                if check(i,j-1):
                    que.append((i,j-1))
                
        print(bd)    
        return bd[0][0]
        
        
        
