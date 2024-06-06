class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []

        for c in range(ord('a'), ord('z')+1):
            c = chr(c)
            min_cnt = float('inf')

            for w in words:
                count = w.count(c)
                min_cnt = min(min_cnt, count)
                if min_cnt == 0:
                    break

            res += [c] * min_cnt

        return res