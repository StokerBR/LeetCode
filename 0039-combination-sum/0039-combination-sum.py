class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remaining, currCombination, start, res):
            if remaining < 0:
                return

            if remaining == 0:
                res.append(currCombination)
                return
            for i in range(start, len(candidates)):
                n = candidates[i]
                backtrack(remaining-n, currCombination+[n], i, res)

        res = []
        backtrack(target, [], 0, res)
        return res