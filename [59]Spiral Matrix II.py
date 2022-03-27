# Given a positive integer n, generate an n x n matrix filled with elements 
# from 1 to n² in spiral order. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [[1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 20 
#  
#  Related Topics Array Matrix Simulation 👍 2652 👎 165


# leetcode submit region begin(Prohibit modification and deletion)
def fill_contour(matrix, start_id, number):
    n = len(matrix)
    for i in range(start_id, n - start_id):
        matrix[start_id][i] = number
        number += 1

    for i in range(start_id + 1, n - start_id):
        matrix[i][n - start_id - 1] = number
        number += 1

    for i in range(n - start_id - 2, start_id - 1, -1):
        matrix[n - start_id - 1][i] = number
        number += 1

    for i in range(n - start_id - 2, start_id, -1):
        matrix[i][start_id] = number
        number += 1
    return number


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[None]*n for _ in range(n)]
        number = 1
        i = 0
        while number <= n*n:
            number = fill_contour(result, i, number)
            i += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
