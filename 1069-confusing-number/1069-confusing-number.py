class Solution:
    def confusingNumber(self, n: int) -> bool:
        nums = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6,
        }

        strNum = str(n)
        res = ''

        for i in range(len(strNum)-1, -1, -1):
            num = int(strNum[i])
            if num in nums:
                res += str(nums[num])
            else:
                return False
        
        return res != strNum