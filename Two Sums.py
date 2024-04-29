#my solution:
#Brute force: similar to contain duplicates, so we use two pointers to add up the numbers 
#and if it's true then return indices, else return an empty array to indicate false
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []