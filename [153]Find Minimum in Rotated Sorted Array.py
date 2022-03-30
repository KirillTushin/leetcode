# Suppose an array of length n sorted in ascending order is rotated between 1 
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might become: 
# 
#  
#  [4,5,6,7,0,1,2] if it was rotated 4 times. 
#  [0,1,2,4,5,6,7] if it was rotated 7 times. 
#  
# 
#  Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results 
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]]. 
# 
#  Given the sorted rotated array nums of unique elements, return the minimum 
# element of this array. 
# 
#  You must write an algorithm that runs in O(log n) time. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 
# times.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
# 
#  
# 
#  
#  Constraints: 
# 
#  
#  n == nums.length 
#  1 <= n <= 5000 
#  -5000 <= nums[i] <= 5000 
#  All the integers of nums are unique. 
#  nums is sorted and rotated between 1 and n times. 
#  
#  Related Topics Array Binary Search 👍 6351 👎 376


# leetcode submit region begin(Prohibit modification and deletion)

def binary_search_max(nums, start_id):
    len_nums = len(nums)
    if len_nums <= 1:
        return start_id

    central_id = len_nums//2

    if nums[0] <= nums[central_id]:
        return binary_search_max(nums[central_id:], start_id + central_id)
    if nums[0] > nums[central_id]:
        return binary_search_max(nums[:central_id], start_id)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        max_id = binary_search_max(nums, 0)
        min_id = (max_id + 1) % len(nums)
        return nums[min_id]
# leetcode submit region end(Prohibit modification and deletion)
