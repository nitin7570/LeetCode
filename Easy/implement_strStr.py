'''
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0
'''

class Solution:
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        elif needle != "" and haystack == "":
            return -1
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1


if __name__ == '__main__':
    haystack = input()
    needle = input()
    solution = Solution()
    print(solution.strStr(haystack, needle))
        