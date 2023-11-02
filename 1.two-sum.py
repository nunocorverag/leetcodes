#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        HashMap = dict()
        for i,n in enumerate(nums):
            num2search = target - n
            if num2search in HashMap:
                return [HashMap[num2search], i]
            #Update hashmap
            HashMap[n] = i
            # print(HashMap)
        
# @lc code=end

