'''
Example 1:
Input: s = "Hello World"
Output: 5

Example 2:
Input: s = " "
Output: 0
'''

class Solution:
    def lengthOfLastWord(self, s):
        word_list = s.strip().split(' ')
        return len(word_list[(len(word_list)-1)])
        
    
if __name__ == '__main__':
    s = input()
    solution = Solution()
    print(solution.lengthOfLastWord(s))