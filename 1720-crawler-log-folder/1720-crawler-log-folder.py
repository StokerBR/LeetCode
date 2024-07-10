class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for log in logs:
            if log == '../':
                res = res-1 if res > 0 else res
            elif log == './':
                continue
            else:
                res += 1
        return res