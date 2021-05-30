'''
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
'''

class Solution(object):
    def isValid(self, s):
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for element in s:
            if element in pairs:
                stack.append(element)
            elif stack and pairs[stack.pop()] == element:
                continue
            else:
                return False
        if len(stack) == 0:
            return True


if __name__ == '__main__':
    s = input().strip()
    solution = Solution()
    print(solution.isValid(s))