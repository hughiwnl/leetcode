class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range (n-1):
            for j in range (i+1,n): #remember that in python for range, its (start, go until but not, by)
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
'''