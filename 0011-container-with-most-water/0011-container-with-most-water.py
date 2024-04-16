class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(height)-1
        lMax, rMax = height[l], height[r]
        while l < r:
            area = min(lMax, rMax) * (r - l)
            maxWater = max(area, maxWater)
            if lMax < rMax:
                l += 1
                lMax = max(height[l], lMax)
            else:
                r -= 1
                rMax = max(height[r], rMax)
        return maxWater
