class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i < j:
            l = s[i].lower()
            r = s[j].lower()
            if l.isalnum() and r.isalnum():
                if l != r:
                    return False
                i += 1
                j -= 1
            else:
                if not l.isalnum():
                    i += 1
                if not r.isalnum():
                    j -= 1
        return True