class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ''
        q = deque(spaces)
        for i, l in enumerate(s):
            if len(q) == 0:
                ans += s[i:]
                break
            if i == q[0]:
                ans += ' '
                q.popleft()
            ans += l
        return ans
            