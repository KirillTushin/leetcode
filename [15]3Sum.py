# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
#  Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#  Example 2: 
#  Input: nums = []
# Output: []
#  Example 3: 
#  Input: nums = [0]
# Output: []
#  
#  
#  Constraints: 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics Array Two Pointers Sorting 👍 16657 👎 1599


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub_dict = {
            value: index
            for index, value in enumerate(nums)
        }

        result = set()
        for index, value in enumerate(nums):
            if target - value in sub_dict:
                sub_index = sub_dict[target - value]
                if sub_index != index:
                    to_add = tuple(sorted((value, target - value)))
                    result.add(to_add)

        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        for i, element in enumerate(nums):
            res = self.twoSum(nums[i+1:], -element)
            for value2, value3 in res:
                to_add = tuple(sorted((element, value2, value3)))
                result.add(to_add)

        return result
# leetcode submit region end(Prohibit modification and deletion)
