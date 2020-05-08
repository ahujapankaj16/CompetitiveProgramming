'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

'''




import math
def calcDist(a,b):
    if b[0]-a[0] != 0:
        d = abs((b[1]-a[1])/(b[0]-a[0]))
        return d
    else:
        return math.inf
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        if len(coordinates) == 2:
            return True
        
        dist=calcDist(coordinates[0],coordinates[1])
        print(dist)
        for i in range(1,len(coordinates)-1):
            if dist!= calcDist(coordinates[i],coordinates[i+1]):
                return False

        return True
