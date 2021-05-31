# --*-- coding:utf-8 --*--
"""
给定一个直方图(也称柱状图)，假设有人从上面源源不断地倒水，最后直方图能存多少水量?直方图的宽度为 1。

上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的直方图，在这种情况下，可以接 6 个单位的水（蓝色部分表示水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/volume-of-histogram-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

def trap1(height):
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

def trap(height) -> int:
    start = 0
    end = len(height) - 1
    result = []
    max = 0
    while start < end:
        if height[start] == 0:
            start += 1
            continue
        if height[end] == 0:
            end -= 1
            continue

        if height[start] > height[end]:
            tmp = height[end]
            tmp_res = [tmp, start, end]
            end -= 1
        else:
            tmp = height[start]
            tmp_res = [tmp, start, end]
            start += 1
        if tmp > max:
            result.append(tmp_res)
            max = tmp
    res = 0
    for item in result:
        aim = item[0]
        start = item[1]
        end = item[2]
        index = start + 1
        while index < end:
            if aim > height[index]:
                res += aim - height[index]
                height[index] = aim
            index += 1
    return res
print(trap1([0,1,0,2,1,0,1,3,2,1,2,1]))