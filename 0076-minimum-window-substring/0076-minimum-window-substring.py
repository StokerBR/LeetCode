class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        freqT, freqS = {}, {}
        res, resLen = (-1,1), float('inf')
        have, need = 0, len(t)
        l = 0

        for c in t:
            freqT[c] = 1 + freqT.get(c, 0)
        
        for r, c in enumerate(s):
            if c in freqT:
                freqS[c] = 1 + freqS.get(c, 0)
                if freqS[c] <= freqT[c]:
                    have += 1

            while have == need:
                if r-l+1 < resLen:
                    res = (l, r)
                    resLen = r-l+1
                if s[l] in freqS:
                    freqS[s[l]] -= 1
                    have -= 1 if freqS[s[l]] < freqT[s[l]] else 0
                l +=1
                
        return s[res[0]:res[1]+1] if resLen != float('inf') else ''