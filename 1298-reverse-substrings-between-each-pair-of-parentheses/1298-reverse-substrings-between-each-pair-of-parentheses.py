class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = ''
        inside = ''
        opened = 0

        for c in s:
            if c == '(':
                if opened > 0:
                    inside += c
                opened += 1
            elif c == ')':
                opened -= 1
                if opened > 0:
                    inside += c
                if opened == 0:
                    res += self.reverseParentheses(inside)[::-1]
                    inside = ''
            elif opened == 0:
                res += c
            else:
                inside += c
        
        return res
            