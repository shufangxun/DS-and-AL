class Solution:
    def twoSum(self, nums, target):
            dict = {}
            for i, num in enumerate(nums):
                if num in dict:
                    return [dict[num], i]
                else:
                    dict[target-num] = i