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
        if size  < 3:
            return size
        ans = 0
        for i in range(size):
            d = {'inf':0}
            samePoint = 1
            for j in range(size):
                if i == j:
                    continue
                elif points[i].x == points[j].x and points[i].y != points[j].y:
                    d['inf'] += 1
                elif points[i].x != points[j].x:
                    k = 1.0 * (points[i].y - points[j].y) / (points[i].x - points[j].x)
                    if k in d:
                        d[k] += 1
                    else:
                        d[k] = 1
                else:
                    samePoint += 1
            ans = max(ans,max(d.values()) + samePoint)
        return ans


if __name__ == '__main__':
    points = [Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 1)]
    ret = Solution().maxPoints(points)
    print(ret)
