class Solution:
    def isValid(self, s: str) -> bool:
        open = []
        eq = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for c in s:
            if c in eq.values():
                open.append(c)
            elif open and open[-1] == eq[c]:
                open.pop()
            else:
                return False
        return True if not open else False