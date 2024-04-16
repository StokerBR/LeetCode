class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)
        seqStarts = set()

        for i, n in enumerate(nums):
            count = 0
            # check if the current number is the start of a new sequence
            if (n-1 not in nums and n not in seqStarts):
                seqStarts.add(n)
                while (n+count) in nums:
                    count += 1
            longest = max(count, longest)
            
        return longest