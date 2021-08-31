"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。



示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]


提示：

1 <= n <= 20
"""

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [([0] * n) for _ in range(n)]
        i = 0
        j = 0
        toward = 0
        maxi = n -1
        maxj = n -1
        mini = 1
        minj = 0
        for item in range(1,n*n + 1):
            result[i][j] = item
            if toward == 1:
                i += 1
                if i == maxi:
                    toward += 1
                    maxi -= 1
            elif toward == 0:
                j += 1
                if j == maxj:
                    toward += 1
                    maxj -= 1
            elif toward == 3:
                i -= 1
                if i == mini:
                    toward += 1
                    mini += 1
            elif toward == 2:
                j -= 1
                if j == minj:
                    toward += 1
                    minj += 1
            toward %= 4
        return result