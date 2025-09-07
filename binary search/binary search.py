class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        # left and right points
        while l <= r:
            mid = (l + r) // 2
            # we have a mid and the // drops the remainder
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1 #move pointer 1 up from mid since we know its not mid, and then we check again
            else: #if its not mid and not less, then its more, so right is mid minus 1
                r = mid - 1
        return -1