class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        num = ''
        neg = False
        for i, c in enumerate(s):
            if c.isnumeric() or (i == 0 and c in ['-', '+'] and (len(s) > 1 and s[i+1].isnumeric())):
                num += c
            else:
                break
        res = int(num) if len(num) > 0 else 0
        limit = pow(2, 31)
        if res < -limit: res = -limit
        if res >= limit: res = (limit) - 1
        return res