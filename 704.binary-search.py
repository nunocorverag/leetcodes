#
# @lc app=leetcode id=704 lang=python
#
# [704] Binary Search
#

# @lc code=start
class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid = -1

        while left <= right:
            # We get the average to found the mid and split the array in 2
            mid = (left + right) //2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            # Mid == Target, we found it
            else:
                return mid
        return -1

# @lc code=end

