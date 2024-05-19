class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left, right):
        bisect.insort_left(self.intervals, [left, right])

        res = [self.intervals[0]]
        for interval in self.intervals:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        self.intervals = res
		
    def queryRange(self, left, right):
        i = bisect.bisect_right(self.intervals, [left, float('inf')])

        if not self.intervals or i == 0:
            return False
        
        return self.intervals[i-1][1] >= right

    def removeRange(self, left, right):
        res = []
        for interval in self.intervals:
            if left <= interval[0] and right >= interval[1]:
                continue
            elif left >= interval[1] or right <= interval[0]:
                res.append(interval)
            elif left < interval[0]:
                res.append([right, interval[1]])
            elif right > interval[1]:
                res.append([interval[0], left])
            else:
                res.append([interval[0], left])
                res.append([right, interval[1]])

        self.intervals = res