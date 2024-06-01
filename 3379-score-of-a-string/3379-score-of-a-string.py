class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = ord(s[0])
        total = 0
        for c in s:
            curr = ord(c)
            total += abs(prev - curr)
            prev = curr
        return total