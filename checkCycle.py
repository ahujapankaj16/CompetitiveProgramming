'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



'''







from collections import defaultdict 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict()
        for i in range(numCourses):
            indegree[i]=0
            graph[i]=[]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            indegree[edge[0]]+=1
        visited = [False]*numCourses
        queue = [] 
        print(graph)
        for i in range(numCourses): 
            if indegree[i] == 0: 
                queue.append(i)      
        cnt = 0
        
        while queue: 
            u = queue.pop(0)  
            print(u)
            for i in graph[u]: 
                indegree[i] -= 1
                # If in-degree becomes zero, add it to queue 
                if indegree[i] == 0: 
                    queue.append(i) 
            cnt += 1
        print(cnt)
        if cnt != numCourses: 
            return False
        else:
            return True
            
        
