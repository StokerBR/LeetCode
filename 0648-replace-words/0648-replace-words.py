class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary)
        words = sentence.split(' ')

        for i, w in enumerate(words):
            curr = ''
            for c in w:
                curr += c    
                if curr in d:
                    words[i] = curr
                    break
        
        return ' '.join(words)