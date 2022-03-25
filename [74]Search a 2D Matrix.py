# Write an efficient algorithm that searches for a value target in an m x n 
# integer matrix matrix. This matrix has the following properties: 
# 
#  
#  Integers in each row are sorted from left to right. 
#  The first integer of each row is greater than the last integer of the 
# previous row. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -10⁴ <= matrix[i][j], target <= 10⁴ 
#  
#  Related Topics Array Binary Search Matrix 👍 6404 👎 250


# leetcode submit region begin(Prohibit modification and deletion)
def find_in_row(row, target):
    row_len = len(row)
    if row_len == 1:
        if target == row[0]:
            return True
        else:
            return False

    middle_id = row_len // 2
    if target == row[middle_id]:
        return True
    elif target < row[middle_id]:
        return find_in_row(row[:middle_id], target)
    else:
        return find_in_row(row[middle_id:], target)


def find_in_matrix(matrix, target):
    matrix_len = len(matrix)
    if matrix_len == 1:
        return find_in_row(matrix[0], target)
    
    middle_id = matrix_len // 2

    middle_row = matrix[middle_id]
    first_in_middle_row = middle_row[0]
    last_in_middle_row = middle_row[-1]

    if first_in_middle_row <= target <= last_in_middle_row:
        return find_in_row(middle_row, target)
    elif target < first_in_middle_row:
        return find_in_matrix(matrix[:middle_id], target)
    elif target > last_in_middle_row:
        return find_in_matrix(matrix[middle_id:], target)


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return find_in_matrix(matrix, target)

# leetcode submit region end(Prohibit modification and deletion)
