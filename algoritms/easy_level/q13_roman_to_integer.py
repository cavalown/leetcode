class Solution:
    def romanToInt(self, s: str) -> int:
        number_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number_list = [number_dict[item] for item in s]

        result = 0

        for index in range(len(s)):
            if index == len(s)-1:
                result += number_list[-1]
                break
            if number_list[index] >= number_list[index+1]:
                result += number_list[index]
            else:
                result -= number_list[index]
        
        return result
