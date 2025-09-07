class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        
        for n in nums:
            if n in counter:
                counter[n] += 1
            else: 
                counter[n] = 1

        max = -1 # dummy value
        ans = -1

        for key, val in counter.items():
            if val > max:
                max = val
                ans = key
        return ans
# remember key value pairs, every value has a key and if the value is higher than the current max
#then thats the new value, and it will also have a key, which will be the answer, aka the number
# {3:1,4:7,7:8} 7 has the most