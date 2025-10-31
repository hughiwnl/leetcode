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
        