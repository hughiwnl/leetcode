#my solution:
#brute force: use two pointers and use isalnum to check if its alphanumeric and check if the characters equal each other
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while i < j:
            while i<j and not s[i].isalnum(): i+=1
            while i<j and not s[j].isalnum(): j-=1

            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True
# this solution has a pointer at the start and the end and if it's not isalnum, it will skip over it
# and if it is, then it will check whether its equal or not, and then move on to the next character.
    