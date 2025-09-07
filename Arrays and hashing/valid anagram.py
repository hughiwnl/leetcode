#my solution:
class Solution(object):
    def isAnagram(self, s, t):
        count = [0] * 26
        count2 = [0] * 26
        for x in s:
            count[ord(x) - ord('a')] += 1
        for x in t:
            count2[ord(x) - ord('a')] -= 1
        return count == count2
# ascii of x could be 1-26 and that minus ascii of a which is zero equals count of value of the letter and we add and subtract 
'''
print statement to show ascii values, this will be useful in group anagrams
a
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
n
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
g
[2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
r
[2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
a
[3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
m
[3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
n
[3, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
a
[2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
g
[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
a
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
r
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
a
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
m
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
'''
# takes up hella space. 
#this will create two arrays with 26 0's and ascii values will be added/deleted depending on the letter
'''
    The defaultdict in Python is a container defined in the collections
      module. It is a subclass of the built-in dict class and provides a
      default value for the key that does not exist. This means that if a
        key is not found in the dictionary, instead of a KeyError being 
        thrown, a new key is created with the default value.
'''
# knowing this, we can use defaultdict(int) which will create integer values for keys 
#that do not exist
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        
        for x in s:
            count[x] += 1
        
        for x in t:
            count[x] -= 1
        
        for val in count.values():
            if val != 0:
                return False
        
        return True
'''
by using print, we can see the values
adding:
defaultdict(<type 'int'>, {u'a': 1})
defaultdict(<type 'int'>, {u'a': 1, u'n': 1})
defaultdict(<type 'int'>, {u'a': 2, u'n': 1})
defaultdict(<type 'int'>, {u'a': 2, u'g': 1, u'n': 1})
defaultdict(<type 'int'>, {u'a': 2, u'r': 1, u'g': 1, u'n': 1})
defaultdict(<type 'int'>, {u'a': 3, u'r': 1, u'g': 1, u'n': 1})
defaultdict(<type 'int'>, {u'a': 3, u'r': 1, u'm': 1, u'g': 1, u'n': 1})
subtracting:
defaultdict(<type 'int'>, {u'a': 3, u'r': 1, u'm': 1, u'g': 1, u'n': 0})
defaultdict(<type 'int'>, {u'a': 2, u'r': 1, u'm': 1, u'g': 1, u'n': 0})
defaultdict(<type 'int'>, {u'a': 2, u'r': 1, u'm': 1, u'g': 0, u'n': 0})
defaultdict(<type 'int'>, {u'a': 1, u'r': 1, u'm': 1, u'g': 0, u'n': 0})
defaultdict(<type 'int'>, {u'a': 1, u'r': 0, u'm': 1, u'g': 0, u'n': 0})
defaultdict(<type 'int'>, {u'a': 0, u'r': 0, u'm': 1, u'g': 0, u'n': 0})
defaultdict(<type 'int'>, {u'a': 0, u'r': 0, u'm': 0, u'g': 0, u'n': 0})
then it runs the for loops that will check the values in count
'''
class Solution(object):
    def isAnagram(self, s, t):
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
        