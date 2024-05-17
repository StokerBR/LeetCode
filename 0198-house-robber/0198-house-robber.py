class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0,0
        for n in nums:
            tmp = max(prev+n, curr)
            prev = curr
            curr = tmp
        return curr