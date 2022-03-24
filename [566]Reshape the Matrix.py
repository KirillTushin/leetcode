# In MATLAB, there is a handy function called reshape which can reshape an m x 
# n matrix into a new one with a different size r x c keeping its original data. 
# 
#  You are given an m x n matrix mat and two integers r and c representing the 
# number of rows and the number of columns of the wanted reshaped matrix. 
# 
#  The reshaped matrix should be filled with all the elements of the original 
# matrix in the same row-traversing order as they were. 
# 
#  If the reshape operation with given parameters is possible and legal, output 
# the new reshaped matrix; Otherwise, output the original matrix. 
# 
#  
#  Example 1: 
# 
#  
# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]
#  
# 
#  Example 2: 
# 
#  
# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == mat.length 
#  n == mat[i].length 
#  1 <= m, n <= 100 
#  -1000 <= mat[i][j] <= 1000 
#  1 <= r, c <= 300 
#  
#  Related Topics Array Matrix Simulation 👍 2075 👎 236


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if n*m != r*c:
            return mat

        result = []
        line = []
        r_ = 0
        c_ = 0
        N = 0

        while r_ < r:
            while c_ < c:
                c_ += 1
                i, j = divmod(N, n)
                line.append(mat[i][j])
                N += 1
            result.append(line)
            line = []
            c_ = 0
            r_ += 1
        return result
# leetcode submit region end(Prohibit modification and deletion)
