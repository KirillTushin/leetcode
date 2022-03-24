# Write a function to find the longest common prefix string amongst an array of 
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] consists of only lower-case English letters. 
#  
#  Related Topics String 👍 7335 👎 2877


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        basis_string = strs[0]
        k = min([len(s) for s in strs])
        n = len(strs)
        res = 0
        for i in range(k):
            candidate = basis_string[i]
            if n != sum(s[i] == candidate for s in strs):
                break
            res += 1
        return basis_string[:res]
# leetcode submit region end(Prohibit modification and deletion)
