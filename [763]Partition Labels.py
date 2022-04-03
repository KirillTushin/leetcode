# You are given a string s. We want to partition the string into as many parts 
# as possible so that each letter appears in at most one part. 
# 
#  Note that the partition is done so that after concatenating all the parts in 
# order, the resultant string should be s. 
# 
#  Return a list of integers representing the size of these parts. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it 
# splits s into less parts.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "eccbbbbdec"
# Output: [10]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 500 
#  s consists of lowercase English letters. 
#  
#  Related Topics Hash Table Two Pointers String Greedy 👍 7469 👎 284


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}

        ## Analog of ordered set
        letters = list(dict.fromkeys(s))

        for l in letters:
            if l not in intervals:
                left = s.find(l)
                right = s.rfind(l)
                intervals[l] = (left, right)

        intervals_list = list(intervals.values())

        index = 1
        intervals_len = len(intervals_list)
        result = [intervals_list[0]]
        while True:
            if index == intervals_len:
                break
            left_now, right_now = result[-1]
            left_next, right_next = intervals_list[index]
            if right_now > left_next:
                result[-1] = left_now, max(right_now, right_next)
            else:
                result.append((left_next, right_next))
            index += 1

        return [right - left + 1 for left, right in result]
# leetcode submit region end(Prohibit modification and deletion)
