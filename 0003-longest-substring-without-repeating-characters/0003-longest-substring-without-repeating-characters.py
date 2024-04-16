class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        count = 0
        chars = set()
        start = 0
        i = 0
        while i < len(s):
            if s[i] not in chars:
                count += 1
                chars.add(s[i])
                longest = max(count, longest)
                i += 1
            else:
                count = 0
                chars = set()
                start += 1
                i = start
        return longest