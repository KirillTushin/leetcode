# Given a signed 32-bit integer x, return x with its digits reversed. If 
# reversing x causes the value to go outside the signed 32-bit integer range [-2³¹, 2³¹ -
#  1], then return 0. 
# 
#  Assume the environment does not allow you to store 64-bit integers (signed 
# or unsigned). 
# 
#  
#  Example 1: 
# 
#  
# Input: x = 123
# Output: 321
#  
# 
#  Example 2: 
# 
#  
# Input: x = -123
# Output: -321
#  
# 
#  Example 3: 
# 
#  
# Input: x = 120
# Output: 21
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
#  Related Topics Math 👍 6792 👎 9461


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        sign = 1
        if x < 0:
            sign = -1
            x *= sign
        x = str(x)
        new_x = x[::-1]
        new_x = sign*int(new_x)


        if -2**31 <= new_x <= 2**31 - 1:
            return new_x

        return 0

# leetcode submit region end(Prohibit modification and deletion)
