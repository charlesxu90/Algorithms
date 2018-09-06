"""
    Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4

Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

这里我们可以用斜率来记录两条边是否在同一条直线。如果考虑再细一点，由于double有精度的问题，斜率最后用分数来表示。

"""

from decimal import *

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        size = len(points)
        if size < 3:
            return size
        ans = 0
        for i in range(size):
            d = {'inf': 0}
            same_point = 1
            for j in range(size):
                print("i:" +  str(points[i].x) + " " + str(points[i].y))
                print("j:" + str(points[j].x) + " " + str(points[j].y))

                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    d['inf'] += 1
                elif points[i].x != points[j].x:
                    k = Decimal(points[i].y - points[j].y) / (points[i].x - points[j].x)
                    print(k)
                    if k in d:
                        d[k] += 1
                    else:
                        d[k] = 1
                else:
                    same_point += 1
            ans = max(ans, max(d.values()) + same_point)
        return ans


# [[0,0],[94911151,94911150],[94911152,94911151]]
if __name__ == '__main__':
    points = [Point(0,0), Point(94911151,94911150), Point(94911152,94911151)]
    ret = Solution().maxPoints(points)
    print(ret)
