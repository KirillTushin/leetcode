# Given an array of integers nums which is sorted in ascending order, and an 
# integer target, write a function to search target in nums. If target exists, then 
# return its index. Otherwise, return -1. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ < nums[i], target < 10⁴ 
#  All the integers in nums are unique. 
#  nums is sorted in ascending order. 
#  
#  Related Topics Array Binary Search 👍 4462 👎 105


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_index = -1
        right_index = len(nums) - 1

        # nums[left_index] < target <= nums[right_index]
        while right_index - left_index > 1:
            center_index = (left_index + right_index) // 2
            central_val = nums[center_index]
            if central_val == target:
                return center_index
            elif central_val < target:
                left_index = center_index
            else:
                right_index = center_index

        value = nums[right_index]
        if value == target:
            return right_index
        return -1

# leetcode submit region end(Prohibit modification and deletion)
