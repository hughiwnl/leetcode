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
    

#GENERATE PARENTHESIS EXAMPLE
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backTrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack)) # joins it to the stack and removes ""
                return
            
            if openN < n:
                stack.append("(")
                backTrack( openN + 1, closedN ) # recursively calls it for different paths
                stack.pop() #pops the recently added bracket to explore different paths
            if closedN < openN:
                stack.append(")")
                backTrack( openN, closedN + 1)
                stack.pop()
        backTrack(0,0)
        return res
