class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
'''
a little confusing, but the first loops detects if theres a cycle, one pointer moves by 1,
the other moves by 2.
second loop, the second pointer starts on the loop and keeps looping, while the first one moves by 1
until they eventually meet
'''