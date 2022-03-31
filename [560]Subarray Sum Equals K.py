# Given an array of integers nums and an integer k, return the total number of 
# subarrays whose sum equals to k. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1], k = 2
# Output: 2
#  Example 2: 
#  Input: nums = [1,2,3], k = 3
# Output: 2
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -1000 <= nums[i] <= 1000 
#  -10⁷ <= k <= 10⁷ 
#  
#  Related Topics Array Hash Table Prefix Sum 👍 12615 👎 404


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0

        hash_table = {0:1}
        cumulative_sum = 0
        for element in nums:
            cumulative_sum += element
            result += hash_table.get(cumulative_sum - k, 0)
            if cumulative_sum in hash_table:
                hash_table[cumulative_sum] += 1
            else:
                hash_table[cumulative_sum] = 1

        return result
# leetcode submit region end(Prohibit modification and deletion)
