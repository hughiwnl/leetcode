#my solution:
#Brute force: use sort function because it's an anagram and if the letters match up, then its true
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sortS = sorted(s)
        sortT = sorted(t)
        return sortS == sortT

