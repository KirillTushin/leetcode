# Given an array of integers nums sorted in non-decreasing order, find the 
# starting and ending position of a given target value. 
# 
#  If target is not found in the array, return [-1, -1]. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
#  Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#  Example 2: 
#  Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#  Example 3: 
#  Input: nums = [], target = 0
# Output: [-1,-1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums is a non-decreasing array. 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics Array Binary Search 👍 9849 👎 280


# leetcode submit region begin(Prohibit modification and deletion)
def binary_search(nums, target, start_id):
    len_nums = len(nums)
    if len_nums == 0:
        return -1

    if len_nums == 1:
        return start_id if nums[0] == target else -1

    central_subid = len_nums // 2
    left_part = nums[:central_subid]
    right_part = nums[central_subid:]
    if nums[central_subid] == target:
        return start_id + central_subid

    elif target < nums[central_subid]:
        return binary_search(left_part, target, start_id)

    elif target > nums[central_subid]:
        return binary_search(right_part, target, start_id + central_subid)


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        sub_id = binary_search(nums, target, 0)
        if sub_id == -1:
            return [-1, -1]

        left_id = sub_id
        right_id = sub_id
        for i in range(sub_id-1, -1, -1):
            if nums[i] == target:
                left_id -= 1
            else:
                break

        for i in range(sub_id+1, len(nums)):
            if nums[i] == target:
                right_id += 1
            else:
                break

        return [left_id, right_id]
# leetcode submit region end(Prohibit modification and deletion)
