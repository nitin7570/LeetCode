'''
Example 1:
Input: s = "III"
Output: 3

Example 2:
Input: s = "IV"
Output: 4

Example 3:
Input: s = "IX"
Output: 9

Example 4:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution:
    def romanToInt(self, s):
        symbol_dict = {"I": 1, "V": 5, "X": 10, "L":50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        result = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in symbol_dict:
                result += symbol_dict[s[i:i+2]]
                i += 2
            else:
                result += symbol_dict[s[i:i+1]]
                i += 1
        return result


if __name__ == '__main__':
    s = input()
    solution = Solution()
    print(solution.romanToInt(s))