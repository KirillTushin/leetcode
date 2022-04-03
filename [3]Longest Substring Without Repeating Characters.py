# Given a string s, find the length of the longest substring without repeating 
# characters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics Hash Table String Sliding Window 👍 22557 👎 1012


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best_substring_len = 0

        substring = ''
        substring_dict = dict()
        substring_len = 0

        for c_id, c in enumerate(s):
            if c in substring_dict:
                substring_len = 0

                start_of_new_substring = substring_dict[c] + 1
                substring = s[start_of_new_substring:c_id]

                substring_dict = dict()
                for sub_id, sub_c in enumerate(substring, start_of_new_substring):
                    substring_dict[sub_c] = sub_id
                    substring_len += 1

            substring_dict[c] = c_id
            substring += c
            substring_len += 1

            best_substring_len = max(best_substring_len, substring_len)

        return best_substring_len
# leetcode submit region end(Prohibit modification and deletion)
