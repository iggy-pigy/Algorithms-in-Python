import re


def isPalindrome(s):
    def toChar(s):
        s = re.split("[^a-zA-Z\\d]+", s)
        s = ''.join([i for i in s if len(i) > 0]).lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnoprstuvwxyz":
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChar(s))
