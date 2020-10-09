'''


There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

 

Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
'''


from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        
        res = []
        for i in connections:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        visited = set()
        order=[10**7]*n
        low=[10**7]*n
        orde = 0
        def dfs(node,parent):
            nonlocal orde
            order[node] = orde
            low[node] = orde
            orde+=1
            visited.add(node)
            
            for nei in graph[node]:
                if nei==parent:
                    continue
                if nei not in visited:
                    dfs(nei,node)
                low[node] = min(low[node],low[nei])
                if low[nei]>order[node]:
                    res.append([nei,node])
        dfs(0,-1)
        return res
