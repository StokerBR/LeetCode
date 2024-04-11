class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) - k == 0:
            return '0'
        
        digits = []

        for n in num:
            while digits and k > 0 and digits[-1] > n:
                digits.pop()
                k -= 1
            digits.append(n)
        
        if k > 0:
            digits = digits[:-k]

        result = ''.join(digits).lstrip('0')
        return result if len(result) > 0 else '0'