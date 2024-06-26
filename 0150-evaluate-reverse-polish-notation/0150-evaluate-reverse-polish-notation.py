class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(['+', '-', '*', '/'])

        for t in tokens:
            if t in operations:
                right = stack.pop()
                left = stack.pop()

                if t == '+':
                    stack.append(left + right)
                elif t == '-':
                    stack.append(left - right)
                elif t == '*':
                    stack.append(left * right)
                elif t == '/':
                    stack.append(int(left / right))
            else:
                stack.append(int(t))

        return stack[-1]