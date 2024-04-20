class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        minNum = float('inf')
        while l < r:
            m = (l+r) // 2
            minNum = min(nums[m], minNum)
            minNum = min(nums[l], minNum)
            minNum = min(nums[r], minNum)
            if nums[l] > nums[m]:
                r = m-1
            elif nums[r] < nums[m]:
                l = m+1
            elif nums[l] < nums[m]:
                r = m-1
            elif nums[r] > nums[m]:
                l = m+1
            #print(m, l, r)
        return minNum