class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0
        r = len(height) - 1
        res = 0
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]
        return res
        
'''
two pointers, the bottleneck will always be the smaller number, so by subtracting the max by the current height, you can find how much water is stored
by setting left max first, you will always subtract the max, which is why there isnt a negative value
'''