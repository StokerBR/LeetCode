class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            if i == len(nums) - 2:
                break
            l, r = i+1, len(nums)-1
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum == 0:
                    solution.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return solution