class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = []
        for (i, n) in enumerate(nums):
            expectedSum = target - n
            if expectedSum in sums:
                return [sums.index(expectedSum), i]
            sums.append(n)