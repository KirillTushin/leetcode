# Given two strings s and p, return an array of all the start indices of p's 
# anagrams in s. You may return the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s and p consist of lowercase English letters. 
#  
#  Related Topics Hash Table String Sliding Window 👍 7200 👎 251


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        s_len = len(s)

        p_counter = collections.Counter(p)
        now_counter = collections.Counter(s[:p_len])

        result = []
        for end_id in range(p_len, s_len):
            start_id = end_id - p_len

            if p_counter == now_counter:
                result.append(start_id)

            start_letter = s[start_id]
            end_letter = s[end_id]

            now_counter[start_letter] -= 1
            if now_counter[start_letter] == 0:
                now_counter.pop(start_letter)

            now_counter[end_letter] += 1

        if p_counter == now_counter:
            result.append(s_len - p_len)

        return result
# leetcode submit region end(Prohibit modification and deletion)
