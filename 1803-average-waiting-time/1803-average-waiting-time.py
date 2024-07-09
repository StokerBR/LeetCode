import statistics
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitingTimes = []
        currTime = 0

        for a, t in customers:
            time = currTime if currTime > a else a
            time += t
            currTime = time
            waitingTimes.append(time - a)
        
        return statistics.mean(waitingTimes)