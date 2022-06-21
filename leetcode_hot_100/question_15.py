class Solution:
    def qsort(self, datas):
        if len(datas) <= 1:
            return datas
        tmp = datas[0]
        updatas = []
        lowdatas = []
        for item in datas[1:]:
            if item > tmp:
                updatas.append(item)
            elif item <= tmp:
                lowdatas.append(item)
        result = self.qsort(lowdatas)
        result.append(tmp)
        result.extend(self.qsort(updatas))
        return result

    def findData(self, datas, targetindex):
        if targetindex == 0:
            start = 1
        else:
            start = 0
        len_data = len(datas)
        if targetindex == len_data - 1:
            end = len_data - 2
        else:
            end = len_data - 1
        target = datas[targetindex] * -1
        result = []
        while start < end:
            if datas[start] + datas[end] == target:
                result.append(self.qsort([datas[start], datas[end], target]))
                start += 1
                if start == targetindex:
                    start += 1
            elif datas[start] + datas[end] > target:
                end -= 1
                if end == targetindex:
                    end -= 1
            else:
                start += 1
                if start == targetindex:
                    start += 1
        return result

    def encode(self, datas):
        return str(datas[0]) + str(datas[1]) + str(datas[2])

    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        result = {}
        targets = {}
        nums = self.qsort(nums)
        index = 0

        while index < len(nums):
            if nums[index] not in targets:
                targets[nums[index]] = 1
                tmps = self.findData(nums, index)
                for item in tmps:
                    code = self.encode(item)
                    if code not in result:
                        result[code] = item
            index += 1
        return result.values()

s = Solution()
s.threeSum([-1,0,1,2,-1,-4])