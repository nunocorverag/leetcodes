#
# @lc app=leetcode id=1089 lang=python
#
# [1089] Duplicate Zeros
#

# @lc code=start
class Solution(object):
    def duplicateZeros(self, arr):
        i = 0
        while i < len(arr):
            if arr[i] == 0 and i != len(arr) - 1:
                for j in range(len(arr) - 1, i, -1):
                    arr[j] = arr[j - 1]
                arr[i + 1] = 0
                i += 1
            i += 1
        """
        Do not return anything, modify arr in-place instead.
        """
        
# @lc code=end

