#neetcode solution
#dictionary = hashmap btw, key value pairs
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {} # use hashmap to count occurences of each value, k
        freq = [[] for i in range(len(nums) + 1)] # this will be the array depending on the length of nums
        #this will create an array in this array for however many values are in nums
        for n in nums:
            count[n] = 1 + count.get(n,0)
        # for every value in nums, we get that value from hashmap count and add 1 + whatever value was already there
        # and if it's empty, then we add 0
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1): #starts here, goes here, by this
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        