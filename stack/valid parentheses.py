class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] # empty list
        map = { ')':'(' , ']':'[' , '}':'{' } # mapping key values, key ) has a value of (
        for c in s:
            if c in map: # for every character in the string, if it's in map then its a closing bracket
                if stack and stack[-1] == map[c]: # we then check if the stack exists and if the most recent one [-1] equals map of the closing bracket
                    stack.pop() # removes the recent added element, we don't add the closing bracket
                else:
                    return False
            else: 
                stack.append(c)
        return True if not stack else False
    
'''
for every character in s, if its not a closing bracket append, it else, if its a closing bracket
check if stack[-1] aka the most recent element is equal to map of c which should be a open bracket
if it is then pop else false.
'''