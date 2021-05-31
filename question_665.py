# --*-- coding:utf-8 --*--

"""
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。

 

示例 1:

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
 

提示：

1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-decreasing-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def check(self,nums):
        index = 1
        while index < len(nums):
            if nums[index -1] > nums[index]:
                return False
            index += 1
        return True

    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 0 or len(nums) == 1:
            return True
        index = 1
        max = min(nums)
        while index < len(nums):
            if nums[index-1] > nums[index]:
                tmp = nums[index-1]
                nums[index-1] = max
                flag1 = self.check(nums)
                if flag1:
                    return True
                nums[index-1] = tmp
                if nums[index-1] > max:
                    nums[index] = nums[index-1]
                else:
                    nums[index] = max
                flag2 = self.check(nums)
                if flag2:
                    return True
                return False
            if nums[index] > max:
                max = nums[index-1]
            index += 1
        return True