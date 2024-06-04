class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        sub = []
        count = collections.defaultdict(int)

        for arr in arrays:
            for n in arr:
                count[n] += 1

        for (n, cnt) in count.items():
            if cnt == len(arrays):
                sub.append(n)

        return sub