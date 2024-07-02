class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq=[0]*1001
        for x in nums1:
            freq[x] += 1

        res = []
        for x in nums2:
            if  freq[x] > 0:
                res.append(x)
                freq[x] -= 1
        return res