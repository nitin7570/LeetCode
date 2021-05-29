'''
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
'''

class Solution(object):
    def twoSum(self, nums, target):
        for key, value in enumerate(nums):
            remainder = target - value
            if remainder in nums[key+1:]:
                index = nums[key+1:].index(remainder) + key+1
                return [key, index]


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    target = int(input())
    solution = Solution()
    print(solution.twoSum(nums, target))