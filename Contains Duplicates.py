# my solution:
# Thought process: Brute force by using two pointers to iterate through array to find duplicates
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    return True
            return False
        
#optimal solution using hashsets
#To make the runtime O(N) we can use hashsets which stores unique values
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = set()
        for n in nums:
            if n in count:
                return True
            count.add(n)
        return False