class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range (n-1):
            for j in range (i+1,n): #remember that in python for range, its (start, go until but not, by)
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []