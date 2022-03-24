# Given an integer numRows, return the first numRows of Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
# 
#  
#  Example 1: 
#  Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  Example 2: 
#  Input: numRows = 1
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= numRows <= 30 
#  
#  Related Topics Array Dynamic Programming 👍 5243 👎 201


# leetcode submit region begin(Prohibit modification and deletion)
def generate_row(prev_row):
    result = []
    for i in range(len(prev_row) - 1):
        result.append(prev_row[i] + prev_row[i+1])
    return [1] + result + [1]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for _ in range(numRows - 1):
            prev_row = result[-1]
            result.append(generate_row(prev_row))
        return result
# leetcode submit region end(Prohibit modification and deletion)
