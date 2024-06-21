class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        already_satisfied = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
                customers[i] = 0
        
        max_satisfied = 0
        current_satisfied = 0
        for i, c in enumerate(customers):
            current_satisfied += c
            if i >= minutes:
                current_satisfied -= customers[i - minutes]
            max_satisfied = max(max_satisfied, current_satisfied)
        
        return already_satisfied + max_satisfied
        