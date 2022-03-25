# Given an array nums of size n, return the majority element. 
# 
#  The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array. 
# 
#  
#  Example 1: 
#  Input: nums = [3,2,3]
# Output: 3
#  Example 2: 
#  Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 5 * 10⁴ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  
# 
#  
# Follow-up: Could you solve the problem in linear time and in O(1) space? 
# Related Topics Array Hash Table Divide and Conquer Sorting Counting 👍 9113 👎 328


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        return counter.most_common(1)[0][0]
# leetcode submit region end(Prohibit modification and deletion)
