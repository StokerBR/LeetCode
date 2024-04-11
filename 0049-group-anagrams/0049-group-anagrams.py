class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for wrd in strs:
            wrdSorted = list(wrd)
            wrdSorted.sort()
            wrdSorted = ''.join(wrdSorted)
            if wrdSorted not in anagrams.keys():
                anagrams[wrdSorted] = []
            anagrams[wrdSorted].append(wrd)
        return anagrams.values()