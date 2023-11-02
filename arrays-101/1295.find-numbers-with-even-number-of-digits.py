#
# @lc app=leetcode id=1295 lang=python
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
class Solution(object):
    def findNumbers(self, nums):
        even_n = 0
        for i in range(len(nums)):
            n_digit = 0
            number = nums[i]
            while number != 0:
                number //= 10
                n_digit += 1
            if n_digit % 2 == 0:
                even_n += 1
        return even_n
        
# @lc code=end

