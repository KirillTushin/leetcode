# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 
# 'C', 'G', and 'T'. 
# 
#  
#  For example, "ACGAATTCCG" is a DNA sequence. 
#  
# 
#  When studying DNA, it is useful to identify repeated sequences within the 
# DNA. 
# 
#  Given a string s that represents a DNA sequence, return all the 10-letter-
# long sequences (substrings) that occur more than once in a DNA molecule. You may 
# return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
#  Example 2: 
#  Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] is either 'A', 'C', 'G', or 'T'. 
#  
#  Related Topics Hash Table String Bit Manipulation Sliding Window Rolling 
# Hash Hash Function 👍 1914 👎 403


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        now_key = s[:10]
        hash_table = {now_key:1}
        result = set()
        for c in s[10:]:
            now_key = (now_key + c)[1:]
            if now_key in hash_table:
                result.add(now_key)
            else:
                hash_table[now_key] = 1
        return list(result)
# leetcode submit region end(Prohibit modification and deletion)
