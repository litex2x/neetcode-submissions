class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,f = 0, len(s)-1
        while i<f:
            while i<f and not self.isAlphaNum(s[i]):
                i += 1
            while i<f and not self.isAlphaNum(s[f]):
                f -= 1
            if s[i].lower() != s[f].lower():
                return False
            i += 1
            f -= 1
        return True

    def isAlphaNum(self, c):
        return (ord('a') <= ord(c.lower()) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))