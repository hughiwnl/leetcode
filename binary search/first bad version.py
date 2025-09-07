# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1,n

        while (l < r):
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid
            else: 
                l = mid + 1
        return l

        
# same as binary search, 1 + 5 = 6 / 2 = 3 and 3 isnt bad so L = 2
# 2 + 5 = 7 / 3 = 3.5 = 3 isnt 4 so L = 3
# so 3 + 5 = 8 // 2 = 4 which is right and this sets r to mid which stops the while loop