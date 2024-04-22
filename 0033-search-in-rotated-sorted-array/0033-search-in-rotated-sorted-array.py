class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            
            if nums[l] > nums[m] and (target > nums[l] or target < nums[m]):
                r = m-1
            elif nums[r] < nums[m] and (target < nums[r] or target > nums[m]):
                l = m+1
            elif target > nums[m]:
                l = m+1
            else:
                r = m-1
        return -1