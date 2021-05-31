# --*-- coding:utf-8 --*--

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        len_h = len(height)
        left = [0] * len_h
        right = [0] * len_h
        index = 1
        max = 0
        while index < len_h:
            if max <= height[index - 1]:
                max = height[index - 1]
            left[index] = max
            index += 1
        index = len_h - 1
        max = 0
        while index >= 1:
            if max <= height[index]:
                max = height[index]
            right[index - 1] = max
            index -= 1

        index = 0
        result = 0
        while index < len_h:
            h = min(left[index], right[index])
            tmp = h - height[index]
            if tmp > 0:
                result += tmp
            index += 1
        return result
