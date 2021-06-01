'''
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

Example 3:
Input: digits = [0]
Output: [1]

'''

class Solution:
    def plusOne(self, digits):
        number = int("".join(str(digit) for digit in digits)) + 1
        number = str(number)
        digits_list = []
        digits_list[:0] = number
        return digits_list
    
    
if __name__ == '__main__':
    digits = list(map(int, input().strip().split()))
    solution = Solution()
    print(solution.plusOne(digits))