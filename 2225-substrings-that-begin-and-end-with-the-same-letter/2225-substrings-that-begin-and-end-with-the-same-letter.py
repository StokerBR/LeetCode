class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        chars = collections.defaultdict(int)
        for c in s:
            chars[c] += 1
            res += chars[c]
        return res