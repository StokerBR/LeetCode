class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}

        for c in s1:
            freq[c] = 1 + freq.get(c, 0)

        freq2 = {}
        l = 0

        for r in range(len(s2)):
            if r-l+1 > len(s1):
                if s2[l] in freq2:
                    freq2[s2[l]] -= 0 if freq2[s2[l]] == 0 else 1
                l += 1

            if s2[r] not in freq:
                freq2 = {}
                l = r
            else:
                freq2[s2[r]] = 1 + freq2.get(s2[r], 0)

            if freq2 == freq:
                return True

        print(freq, freq2)
        return False