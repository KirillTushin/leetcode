# Given a string s which consists of lowercase or uppercase letters, return the 
# length of the longest palindrome that can be built with those letters. 
# 
#  Letters are case sensitive, for example, "Aa" is not considered a palindrome 
# here. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abccccdd"
# Output: 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "a"
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: s = "bb"
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2000 
#  s consists of lowercase and/or uppercase English letters only. 
#  
#  Related Topics Hash Table String Greedy 👍 2528 👎 150


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0
        used_one = False
        for key, value in counter.items():
            res += (value // 2) * 2
            if value % 2 == 1 and not used_one:
                res += 1
                used_one = True
        return res
# leetcode submit region end(Prohibit modification and deletion)
