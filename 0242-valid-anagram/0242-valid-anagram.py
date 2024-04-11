class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sList = list(s)
        sList.sort()
        tList = list(t)
        tList.sort()

        return ''.join(sList) == ''.join(tList)