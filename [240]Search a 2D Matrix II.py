# Write an efficient algorithm that searches for a value target in an m x n 
# integer matrix matrix. This matrix has the following properties: 
# 
#  
#  Integers in each row are sorted in ascending from left to right. 
#  Integers in each column are sorted in ascending from top to bottom. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[1
# 8,21,23,26,30]], target = 5
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[1
# 8,21,23,26,30]], target = 20
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= n, m <= 300 
#  -10⁹ <= matrix[i][j] <= 10⁹ 
#  All the integers in each row are sorted in ascending order. 
#  All the integers in each column are sorted in ascending order. 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics Array Binary Search Divide and Conquer Matrix 👍 6942 👎 121


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        current_row = m - 1
        current_column = 0

        while True:
            current_value = matrix[current_row][current_column]
            if current_value == target:
                return True

            if current_value > target:
                if current_row == 0:
                    return False
                current_row -= 1

            else:
                if current_column == n - 1:
                    return False
                current_column += 1
# leetcode submit region end(Prohibit modification and deletion)
