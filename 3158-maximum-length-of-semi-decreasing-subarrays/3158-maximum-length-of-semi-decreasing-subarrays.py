class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []

        for i in range(n):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)

        res = 0
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                res = max(res, i - stack[-1] + 1)
                stack.pop()
        
        return res