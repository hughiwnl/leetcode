class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -=1
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1
        return True
# strings are zero indexed meaning that it starts at 0 
    
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        r = len(s) - 1
        while l < r:
            while s[l] is not s[l].isalnum():
                l += 1
            while s[r] is not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True
'''