# Given two strings ransomNote and magazine, return true if ransomNote can be 
# constructed from magazine and false otherwise. 
# 
#  Each letter in magazine can only be used once in ransomNote. 
# 
#  
#  Example 1: 
#  Input: ransomNote = "a", magazine = "b"
# Output: false
#  Example 2: 
#  Input: ransomNote = "aa", magazine = "ab"
# Output: false
#  Example 3: 
#  Input: ransomNote = "aa", magazine = "aab"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= ransomNote.length, magazine.length <= 10⁵ 
#  ransomNote and magazine consist of lowercase English letters. 
#  
#  Related Topics Hash Table String Counting 👍 1582 👎 288


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_collection = collections.Counter(ransomNote)
        magazine_collection = collections.Counter(magazine)

        for key, value in ransom_collection.items():
            if key not in magazine_collection:
                return False

            if value > magazine_collection[key]:
                return False

        return True
# leetcode submit region end(Prohibit modification and deletion)
