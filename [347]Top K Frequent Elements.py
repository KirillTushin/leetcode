# Given an integer array nums and an integer k, return the k most frequent 
# elements. You may return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#  Example 2: 
#  Input: nums = [1], k = 1
# Output: [1]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  k is in the range [1, the number of unique elements in the array]. 
#  It is guaranteed that the answer is unique. 
#  
# 
#  
#  Follow up: Your algorithm's time complexity must be better than O(n log n), 
# where n is the array's size. 
#  Related Topics Array Hash Table Divide and Conquer Sorting Heap (Priority 
# Queue) Bucket Sort Counting Quickselect 👍 8764 👎 359


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1

        sorted_result = sorted(hash_table.items(), key=lambda item: -item[1])[:k]
        return [key for key, value in sorted_result]
# leetcode submit region end(Prohibit modification and deletion)
