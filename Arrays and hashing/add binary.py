class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a,b = a[::-1], b[::-1]

        for i in range(max(len(a),len(b))):
            digitA = ord(a[i]) - ord('0') if i < len(a) else 0
            digitB = ord(b[i]) - ord('0') if i < len(b) else 0 
            # this is to get 1 and 0, and if one of them has a longer string, the digit will just be 0 for the other one that is missing a digit
            '''
            a[i] is '3' (the character at index 2 in the string "12345").
            ord('3') is 51 (the Unicode code point for the character '3').
            ord('0') is 48 (the Unicode code point for the character '0').
            51 - 48 is 3, which is the numerical value of the digit '3'.
            '''
            total = digitA + digitB + carry
            # results in ither 3,2, or 1
            char = str(total % 2)
            # turns result into string, 3%2=1, 2%2=0, 1%2=1
            res = char + res
            #adds it to the res
            carry = total // 2
            # sets carry to 3//2 = 1, 2//2 = 0 or 1//2 = 0
        if carry: # if there's still one carry left over, add to front of res
            res = '1' + res
        return res