# There is an integer array nums sorted in ascending order (with distinct 
# values). 
# 
#  Prior to being passed to your function, nums is possibly rotated at an 
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k]
# , nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For 
# example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0
# ,1,2]. 
# 
#  Given the array nums after the possible rotation and an integer target, 
# return the index of target if it is in nums, or -1 if it is not in nums. 
# 
#  You must write an algorithm with O(log n) runtime complexity. 
# 
#  
#  Example 1: 
#  Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#  Example 2: 
#  Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#  Example 3: 
#  Input: nums = [1], target = 0
# Output: -1
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 5000 
#  -10⁴ <= nums[i] <= 10⁴ 
#  All values of nums are unique. 
#  nums is an ascending array that is possibly rotated. 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics Array Binary Search 👍 13275 👎 866

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


def binary_search(nums, target, start_id):
    len_nums = len(nums)
    if len_nums == 0:
        return -1

    if len_nums == 1:
        return start_id if nums[0] == target else -1

    central_subid = len_nums // 2
    if nums[central_subid] == target:
        return start_id + central_subid

    elif target < nums[central_subid]:
        return binary_search(nums[:central_subid], target, start_id)

    elif target > nums[central_subid]:
        return binary_search(nums[central_subid:], target, start_id + central_subid)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        id_max = binary_search_max(nums, 0)
        if target >= nums[0]:
            return binary_search(nums[:id_max+1], target, 0)
        else:
            return binary_search(nums[id_max+1:], target, id_max + 1)
# leetcode submit region end(Prohibit modification and deletion)
