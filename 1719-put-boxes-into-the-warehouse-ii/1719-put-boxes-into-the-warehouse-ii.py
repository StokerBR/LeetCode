class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        l = 0
        r = len(warehouse)-1
        res = 0
        for box in sorted(boxes, reverse=True): 
            if l <= r: 
                if box <= warehouse[l]: 
                    l += 1
                    res += 1
                elif box <= warehouse[r]: 
                    r -= 1
                    res += 1
        return res