# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, 
# numsr] of which the sum is greater than or equal to target. If there is no such 
# subarray, return 0 instead. 
# 
#  
#  Example 1: 
# 
#  
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem 
# constraint.
#  
# 
#  Example 2: 
# 
#  
# Input: target = 4, nums = [1,4,4]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= target <= 10⁹ 
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁵ 
#  
# 
#  
# Follow up: If you have figured out the O(n) solution, try coding another 
# solution of which the time complexity is O(n log(n)). Related Topics Array Binary 
# Search Sliding Window Prefix Sum 👍 6172 👎 182


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        const = 100001
        result = const
        start_id = 0
        value = 0

        for end_id in range(len(nums)):
            value += nums[end_id]

            if value >= target:
                while value >= target:
                    value -= nums[start_id]
                    start_id += 1
                result = min(result, end_id - start_id + 1 + 1)

        return result if result < const else 0
# leetcode submit region end(Prohibit modification and deletion)