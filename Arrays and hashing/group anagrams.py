'''
IMPORTANT:
In Python, any immutable object (such as an integer, boolean, string, tuple) 
is hashable, meaning its value does not change during its lifetime.
This allows Python to create a unique hash value to identify it, which can
be used by dictionaries to track unique keys and sets to track unique 
values. A tuple is a hashable value and can be used as a dictionary key.
Because lists are mutable, dict keys need to be hashable, and hashing 
mutable objects is a bad idea because hash values should be computed on 
the basis of instance attributes. 
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list) 
        '''
        A defaultdict works exactly like a normal dict, but it is 
        initialized with a function (“default factory”) that takes no 
        arguments and provides the default value for a nonexistent key
        A defaultdict will never raise a KeyError. Any key that does not exist 
        gets the value returned by the default factory.
        '''
        '''
        refer to valid anagram, default dict will create a container defined in the 
        collections module. It is a subclass of the built-in dict class and provides a
      default value for the key that does not exist. This means that if a
        key is not found in the dictionary, instead of a KeyError being 
        thrown, a new key is created with the default value. 
        Which means that it will create a list(array) for each new word 
        '''

        for s in strs:
            count = [0] * 26 

            for c in s:
                count[ord(c) - ord('a')] += 1
                '''
                here, it will create a 26 value list with 0's and after
                it will add 1 for each character for every string in strs
                and every character in s(string)
                '''
            res[tuple(count)].append(s) 
            '''
            we use tule because its immutable so that we can append it to our dictionary
            we append 's' because it's the word itself, if that makes sense
            after it goes through every character, it will append it to the list res
            and if theres no value for res, it will create a new value 
            and also remember that lists are arrays so [["word","drow"],["hey","yeh"]]
            '''
        return res.values() # returns array 

'''
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''