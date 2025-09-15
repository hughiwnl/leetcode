class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #numset is the set of the nums
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet: # if num - 1 not in set, its the start of a seq
                length = 1
                while (num + length) in numSet: # in the loop, if n + 1 in the set, keep going and updating length 
                    length += 1
                longest = max(length, longest)
        return longest
    
'''
numset is the set of the nums

'''