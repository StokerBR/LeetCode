class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.pq = deque()
        self.sl = []
        self.total = 0
        self.start_k = 0
        self.end_k = 0

    def addElement(self, num: int) -> None:
        # insert new element
        self.total += num
        self.pq.append(num)
        i = bisect.bisect_left(self.sl, num)
        if i < self.k:
            self.start_k += num
            if len(self.sl) >= self.k:
                self.start_k -= self.sl[self.k - 1]
        if i >= len(self.sl) - self.k + 1:
            self.end_k += num
            if len(self.sl) >= self.k:
                self.end_k -= self.sl[-self.k]
        self.sl.insert(i, num)

        # remove element
        if len(self.pq) > self.m:
            num = self.pq.popleft()
            self.total -= num
            i = bisect.bisect_left(self.sl, num)
            if i < self.k:
                self.start_k -= num
                self.start_k += self.sl[self.k]
            elif i >= len(self.sl) - self.k:
                self.end_k -= num
                self.end_k += self.sl[-self.k - 1]
            self.sl.pop(i)

    def calculateMKAverage(self) -> int:
        if len(self.sl) < self.m:
            return -1

        return int((self.total - self.start_k - self.end_k) / (self.m - (2 * self.k)))


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()