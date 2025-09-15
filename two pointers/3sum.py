class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort takes O(nlogn) time comp

        for i, a in enumerate(nums): # enumerate creates indexes and values, so that we don't have to keep track of both
            if a > 0: #if it's greather than 0, it wont add to 0 since its sorted
                break

            if i > 0 and a == nums[i - 1]: #if i is greater than 0 (so that it doesnt go to a negative index value) and equals the previous number, go to next i index since its a duplicate
                continue

            l, r = i + 1, len(nums) - 1 # left starts in front of i(a) and r starts at the end
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: # if it adds up and its too big, move right
                    r -= 1 #even if there are duplicates on the right, it will keep moving the right pointer if its bigger than threeSum
                elif threeSum < 0: # if it adds up and its too small, move left
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]]) # else add it to results
                    l += 1 # move pointers to find more 
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r: # it can't have duplicate triplets, but it can have duplicates within
                        l += 1 # so after it adds the first time, the rest is useless, so we will move the left pointer to a new number

        return res