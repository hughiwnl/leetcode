# this problem actually hurt my head, thank god for neetcode
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
        '''
        Encoder, turns every string in the array to 5#world3#lol
        '''
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res = []
        i = 0
        while i < len(str):
            j=i
            while str[j] != '#':
                j+=1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i =  j + 1 + length
        return res
    #iterates over the code, takes the first two numbers and stops and sets it as length
    # uses length to iterate over numbers till the end and thats the decode method
