class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []
        
'''
with two pointers, since it's sorted, 
if left + right is larger than the target then we can move down the right
and if its smaller, than we can move up the left
this way we have O(n) time complexity
'''