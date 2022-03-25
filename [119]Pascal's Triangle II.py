# Given an integer rowIndex, return the rowIndexᵗʰ (0-indexed) row of the 
# Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
# 
#  
#  Example 1: 
#  Input: rowIndex = 3
# Output: [1,3,3,1]
#  Example 2: 
#  Input: rowIndex = 0
# Output: [1]
#  Example 3: 
#  Input: rowIndex = 1
# Output: [1,1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= rowIndex <= 33 
#  
# 
#  
#  Follow up: Could you optimize your algorithm to use only O(rowIndex) extra 
# space? 
#  Related Topics Array Dynamic Programming 👍 2385 👎 259


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        n = rowIndex + 1
        k = 1
        while len(result) < n:
            last = result[-1]
            new = int(last * (n-k) / k)
            result.append(new)
            k += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
