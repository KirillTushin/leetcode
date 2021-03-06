# Implement strStr(). 
# 
#  Return the index of the first occurrence of needle in haystack, or -1 if 
# needle is not part of haystack. 
# 
#  Clarification: 
# 
#  What should we return when needle is an empty string? This is a great 
# question to ask during an interview. 
# 
#  For the purpose of this problem, we will return 0 when needle is an empty 
# string. This is consistent to C's strstr() and Java's indexOf(). 
# 
#  
#  Example 1: 
#  Input: haystack = "hello", needle = "ll"
# Output: 2
#  Example 2: 
#  Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#  Example 3: 
#  Input: haystack = "", needle = ""
# Output: 0
#  
#  
#  Constraints: 
# 
#  
#  0 <= haystack.length, needle.length <= 5 * 10⁴ 
#  haystack and needle consist of only lower-case English characters. 
#  
#  Related Topics Two Pointers String String Matching 👍 3730 👎 3512


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_haystack = len(haystack)

        for i in range(len_haystack - len_needle + 1):
            if needle == haystack[i : i + len_needle]:
                return i

        return -1
# leetcode submit region end(Prohibit modification and deletion)