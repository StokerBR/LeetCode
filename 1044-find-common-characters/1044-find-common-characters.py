class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = collections.defaultdict(list)
        n = len(words)
        for i, w in enumerate(words):
            for c in w:
                if freq[c] == []:
                    freq[c] = [0 for _ in range(n)]
                freq[c][i] += 1

        res = []
        for c, arr in freq.items():
            for _ in range(sorted(arr)[0]):
                res.append(c)
        
        return res