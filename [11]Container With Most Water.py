# You are given an integer array height of length n. There are n vertical lines 
# drawn such that the two endpoints of the iᵗʰ line are (i, 0) and (i, height[i]).
#  
# 
#  Find two lines that together with the x-axis form a container, such that the 
# container contains the most water. 
# 
#  Return the maximum amount of water a container can store. 
# 
#  Notice that you may not slant the container. 
# 
#  
#  Example 1: 
# 
#  
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,
# 3,7]. In this case, the max area of water (blue section) the container can 
# contain is 49.
#  
# 
#  Example 2: 
# 
#  
# Input: height = [1,1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  n == height.length 
#  2 <= n <= 10⁵ 
#  0 <= height[i] <= 10⁴ 
#  
#  Related Topics Array Two Pointers Greedy 👍 15805 👎 915


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        best_area = 0
        while left_index < right_index:
            left_height = height[left_index]
            right_height = height[right_index]
            height_ = min(left_height, right_height)
            now_area = (right_index - left_index) * height_
            best_area = max(now_area, best_area)
            if left_height < right_height:
                left_index += 1
            else:
                right_index -= 1
        return best_area
# leetcode submit region end(Prohibit modification and deletion)
