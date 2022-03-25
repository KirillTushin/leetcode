# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: s = "anagram", t = "nagaram"
# Output: true
#  Example 2: 
#  Input: s = "rat", t = "car"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you 
# adapt your solution to such a case? 
#  Related Topics Hash Table String Sorting 👍 4452 👎 204


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)

        return s_counter == t_counter
# leetcode submit region end(Prohibit modification and deletion)
