class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums): #in each branch, once it hits 3 it will append
                res.append(subset.copy()) # appends to res, basically “Take a photo of what’s in my backpack right now before I change it.”
                return # goes back a level once its max
            subset.append(nums[i]) # add thenumber to subset first
            dfs(i + 1) # goes up one track
            subset.pop() # removes that 
            dfs(i + 1) # goes back one and down the track where that number isnt there
        dfs(0)
        return res