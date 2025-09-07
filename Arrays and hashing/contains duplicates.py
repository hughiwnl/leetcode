class Solution(object):
    def containsDuplicate(self, nums):
        n = len(nums)
        for i in range(n - 1): # out of range since we're using two pointters
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

# its an array so, it will move 1 by one.
# if we do a hashet, we can add it and check if its in the set.