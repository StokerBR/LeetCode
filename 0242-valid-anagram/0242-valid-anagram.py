class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        if len(s) != len(t):
            return False
        for c in s:
            chars[c] = chars.get(c, 0) + 1
        for c in t:
            if c in chars.keys() and chars[c] > 0:
                chars[c] -= 1
            else:
                return False
        return True