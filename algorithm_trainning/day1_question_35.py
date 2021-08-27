"""
35.
搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为
O(log
n) 的算法。



示例
1:

输入: nums = [1, 3, 5, 6], target = 5
输出: 2
示例
2:

输入: nums = [1, 3, 5, 6], target = 2
输出: 1
示例
3:

输入: nums = [1, 3, 5, 6], target = 7
输出: 4
示例
4:

输入: nums = [1, 3, 5, 6], target = 0
输出: 0
示例
5:

输入: nums = [1], target = 0
输出: 0
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        if len(nums) == 0:
            return 1
        elif len(nums) == 1:
            if nums[0] >= target:
                return 0
            else:
                return 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            else:
                if mid > 0 and (nums[mid] - target) * (nums[mid-1] - target) < 0:
                    return mid
                if mid > len(nums) - 2 or (nums[mid] - target) * (nums[mid + 1] - target) < 0:
                    return mid + 1
                if nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
        return mid