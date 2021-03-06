class Solution:
    def permutation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        
        nums.sort()
        res = [] 
        used = [False] * len(nums)
        self.dfs(nums, 0, [], used, res)
        return res
    
    def dfs(self, nums, idx, path, used, res):
        if idx == len(nums):
            res.append(path.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:  ## 判断重复
                    continue
                used[i] = True
                path.append(nums[i])
                self.dfs(nums, idx + 1, path, used, res)
                used[i] = False
                path.pop()   # 为啥pop()

 