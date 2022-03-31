# Given two strings s and t, return true if they are equal when both are typed 
# into empty text editors. '#' means a backspace character. 
# 
#  Note that after backspacing an empty text, the text will continue empty. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
#  
# 
#  Example 3: 
# 
#  
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 200 
#  s and t only contain lowercase letters and '#' characters. 
#  
# 
#  
#  Follow up: Can you solve it in O(n) time and O(1) space? 
#  Related Topics Two Pointers String Stack Simulation 👍 3736 👎 175


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_index = len(s) - 1
        t_index = len(t) - 1

        s_skip_count = 0
        t_skip_count = 0

        while s_index >= 0 or t_index >= 0:

            while s_index >= 0 and s[s_index] == '#':
                s_index -= 1
                s_skip_count += 1

            while s_index >= 0 and s_skip_count and s[s_index] != '#':
                s_index -= 1
                s_skip_count -= 1

            if s_index >= 0:
                if s[s_index] == '#':
                    continue

            while t_index >= 0 and t[t_index] == '#':
                t_index -= 1
                t_skip_count += 1

            while t_index >= 0 and t_skip_count and t[t_index] != '#':
                t_index -= 1
                t_skip_count -= 1

            if t_index >= 0:
                if t[t_index] == '#':
                    continue

            if s_index >= 0 and t_index >= 0:
                if s[s_index] != t[t_index]:
                    return False

            elif s_index >= 0 and t_index < 0:
                return False

            elif s_index < 0 and t_index >= 0:
                return False

            s_index -= 1
            t_index -= 1

        return True
# leetcode submit region end(Prohibit modification and deletion)
