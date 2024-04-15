class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        res = [0] * len(nums)

        for i in range(len(nums)):
            prefix[i] = (prefix[i-1] if i > 0 else 1) * nums[i]
        
        for i in reversed(range(len(nums))):
            postfix[i] = (postfix[i+1] if i < len(nums)-1 else 1) * nums[i]

        for i in range(len(nums)):
            res[i] = (prefix[i-1] if i > 0 else 1) * (postfix[i+1] if i < len(nums)-1 else 1)
        
        return res