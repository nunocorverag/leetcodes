#
# @lc app=leetcode id=34 lang=python
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution(object):
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            right = len(nums) - 1
            left = 0
            mid = None
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                    #if nums[mid] == target -> This means we found a value, we need to go to the leftest one of it
                else:
                    #if mid is in the beggining or the targets is not in the previous position, then we return mid
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    #Go one value backwards and continue iterating
                    else:
                        right = mid - 1
            return -1

        def findLast(nums, target):
            right = len(nums) - 1
            left = 0
            mid = None
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                    else:
                        left = mid + 1
            return -1

        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first, last]
        # This algorithm is O(n) -> Needs to be O(logn) we can implement a binary search
        # i = 0
        # j = len(nums) - 1
        # find = False
        # first = None
        # last = None
        # while i < len(nums) and (find == False):
        #     if nums[i] == target and first == None:
        #         first = i
        #     if nums[j] == target and last == None:
        #         last = j
        #     if first != None and last != None:
        #         return [first, last]
        #     i += 1
        #     j -= 1
        # return [-1, -1]

# @lc code=end

