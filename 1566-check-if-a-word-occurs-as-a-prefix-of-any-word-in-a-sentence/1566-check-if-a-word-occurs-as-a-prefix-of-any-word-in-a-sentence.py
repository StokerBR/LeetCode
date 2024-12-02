class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split()
        for i, w in enumerate(l):
            if w.startswith(searchWord):
                return i+1
        return -1