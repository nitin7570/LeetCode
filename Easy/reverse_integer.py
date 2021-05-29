'''
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
'''

class Solution:
    def reverse(self, x):
        string = "".join(reversed(str(x)))
        if string.endswith('-'):
            string = string[:-1]
            x = -int(string)
        else:
            x = int(string)
        if x >= -2147483648 and x <= 2147483647:
            return x
        else:
            return 0


if __name__ == '__main__':
    x = int(input())
    solution = Solution()
    print(solution.reverse(x))