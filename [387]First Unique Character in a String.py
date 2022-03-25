# Given a string s, find the first non-repeating character in it and return its 
# index. If it does not exist, return -1. 
# 
#  
#  Example 1: 
#  Input: s = "leetcode"
# Output: 0
#  Example 2: 
#  Input: s = "loveleetcode"
# Output: 2
#  Example 3: 
#  Input: s = "aabb"
# Output: -1
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s consists of only lowercase English letters. 
#  
#  Related Topics Hash Table String Queue Counting 👍 4720 👎 189


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_table = collections.defaultdict(int)
        for c in s:
            hash_table[c] += 1

        for index, c in enumerate(s):
            if hash_table[c] == 1:
                return index

        return -1
# leetcode submit region end(Prohibit modification and deletion)
