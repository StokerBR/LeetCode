class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def int_str(num):
            digits = list(str(num))
            for i in range(len(digits)):
                digits[i] = str(mapping[int(digits[i])])
            return int("".join(digits))

        number_mapping = {}
        for num in nums:
            number_mapping[num] = int_str(num)
        nums.sort(key=lambda val: number_mapping[val])

        return nums