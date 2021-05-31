'''
Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0
'''

class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            index = nums.index(target)
            nums.remove(target)
            return index
        

if __name__ == '__main__':
    nums = list(map(int, input().strip().split(' ')))
    target = int(input())
    solution = Solution()
    print(solution.searchInsert(nums, target))