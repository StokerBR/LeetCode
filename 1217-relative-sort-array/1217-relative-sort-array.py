class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res, cnt = [], collections.Counter(arr1)
        for i in arr2:
            for _ in range(cnt.pop(i)):
                res.append(i)
        for i in range(min(arr1), max(arr1) + 1):
            for _ in range(cnt.pop(i, 0)):
                res.append(i)
        return res