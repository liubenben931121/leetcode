"""
977. 有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。



示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]


提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        index = 0
        len_num = len(nums)
        while index < len_num:
            if nums[index] >= 0:
                break
            index += 1
        i = index - 1
        j = index
        while i >= 0 and j < len_num:
            tmp = nums[i] * -1
            if tmp <= nums[j]:
                result.append(tmp * tmp)
                i -= 1
            else:
                result.append(nums[j] * nums[j])
                j += 1

        while i >= 0:
            result.append(nums[i] * nums[i])
            i -= 1
        while j < len_num:
            result.append(nums[j] * nums[j])
            j += 1
        return result