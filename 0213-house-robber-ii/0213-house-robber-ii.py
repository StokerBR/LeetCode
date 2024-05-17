class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robHouses(nums[1:]), self.robHouses(nums[:-1]))
        
    def robHouses(self, nums):
        prev, curr = 0, 0
        for n in nums:
            tmp = max(prev+n, curr)
            prev = curr
            curr = tmp
        return curr