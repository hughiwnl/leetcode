class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")

        return res
    
'''
with pop
res = []
path = []

def dfs(i):
    if i == len(nums):
        res.append(path.copy())
        return
    for num in nums:
        path.append(num)
        dfs(i + 1)
        path.pop()

without pop      
res = []

def dfs(i, path):
    if i == len(nums):
        res.append(path)
        return
    for num in nums:
        dfs(i + 1, path + [num])
        
Here path + [num] creates a new list at each recursion —
so there’s no shared mutation to undo.
Each branch of recursion gets its own “copy” of the state.
'''