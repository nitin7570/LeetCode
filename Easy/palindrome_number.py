'''
Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false
'''

class Solution:
    def isPalindrome(self, x):
        return str(x) == "".join(list(reversed(str(x))))


if __name__ == '__main__':
    x = int(input())
    solution = Solution()
    print(solution.isPalindrome(x))