# 给定M×N矩阵，每一行、每一列都按升序排列，请编写代码找出某元素。
#
#  示例:
#
#  现有矩阵 matrix 如下：
#
#  [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
#
#  给定 target = 5，返回 true。
#
#  给定 target = 20，返回 false。
#  Related Topics 数组 二分查找 分治 矩阵
#  👍 30 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) <= 0 or len(matrix[0]) <= 0:
            return False
        leni = len(matrix)
        lenj = len(matrix[0])
        starti = leni - 1
        startj = 0
        while startj < lenj and starti >= 0:
            if matrix[starti][startj] == target:
                return True
            if matrix[starti][startj] > target:
                starti -= 1
            if matrix[starti][startj] < target:
                startj += 1
        return False

# s = Solution()
# s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
# s.searchMatrix([], 0)

# leetcode submit region end(Prohibit modification and deletion)
