# inefficient
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]

            res[i] = prod
        return res
            
# better solution
# pre fix is the left all multiplied up
# post fix is right all ultiplied up
# imaginary ones outside the array will be postfix and prefix
# how it works is that it will multiply everything before it and put it into the current i

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
[1][2][3][4]
[1][1][2][6]
[24][12][8][6]
