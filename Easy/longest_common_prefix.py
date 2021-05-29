'''
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        else:
            strs.sort()
            result_string = []
            for index, char in enumerate(strs[0]):
                if char == strs[-1][index]:
                    result_string.append(char)
                else:
                    break
            return "".join(result_string)


if __name__ == '__main__':
    strs = list(input().split(' '))
    solution = Solution()
    print(solution.longestCommonPrefix(strs))