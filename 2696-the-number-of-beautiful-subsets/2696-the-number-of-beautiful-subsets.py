class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq = {}
        def f(i: int) -> int:
            if i == len(nums):
                return 1
            result = f(i + 1)
            if not nums[i] - k in freq and not nums[i] + k in freq:
                freq[nums[i]] = freq.get(nums[i], 0) + 1
                result += f(i + 1)
                freq[nums[i]] -= 1
                if freq[nums[i]] == 0:
                    del freq[nums[i]]
            return result
        return f(0) - 1