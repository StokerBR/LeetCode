from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        maxes = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            if d and d[0] == i-k:
                d.popleft()
            d.append(i)
            if i >= k-1:
                maxes.append(nums[d[0]])
        return maxes