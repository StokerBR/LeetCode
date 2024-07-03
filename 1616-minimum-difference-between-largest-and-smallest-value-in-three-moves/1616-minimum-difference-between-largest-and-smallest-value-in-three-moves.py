class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 0:
            return 0

        heapq.heapify(nums)

        small = heapq.nsmallest(4, nums)

        large = heapq.nlargest(4, nums)
        large.reverse()

        return min(x-y for x, y in zip(large, small))