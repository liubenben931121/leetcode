"""
119. 杨辉三角 II
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。





示例 1:

输入: rowIndex = 3
输出: [1,3,3,1]
示例 2:

输入: rowIndex = 0
输出: [1]
示例 3:

输入: rowIndex = 1
输出: [1,1]


提示:

0 <= rowIndex <= 33
"""

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        index = 2
        tmp = [1,1]
        while index <= rowIndex:
            result = [1]
            i = 0
            while i < len(tmp) - 1:
                result.append(tmp[i] + tmp[i + 1])
                i += 1
            result.append(1)
            index += 1
            tmp = result
        return result