class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        work = list(zip(profit, difficulty))
        work.sort(reverse=True)
        worker.sort(reverse=True)
        res = 0
        i = 0
        for w in worker:
            while i < len(work) and w < work[i][1]:
                i += 1
            if i == len(work):
                break
            if w >= work[i][1]:
                res += work[i][0]
        return res