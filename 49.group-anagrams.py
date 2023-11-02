#
# @lc app=leetcode id=49 lang=python
#
# [49] Group Anagrams
#

# @lc code=start

from collections import defaultdict

class Solution(object):

    def groupAnagrams(self, strs):
        #This is used for map the character count of each string and map that to the list of anagrams
        #NOTE: We use the defaultdict method to specify the default value when the dictionary is initialized
        result = defaultdict(list)

        #go through every string
        for s in strs:
            #This list contains 26 elements (26 letters for english alphabet) all initialized on 0
            count = [0] * 26 #a ... z
            #We wanna map a -> 0 and z -> 26
            for c in s:
                #We take the ascii value of the letter and substract the ascii value for a to arrange it from 0 - 26
                count[ord(c) - ord("a")] += 1 #Increment the character by one

            result[tuple(count)].append(s)

        return result.values()
        
# @lc code=end

