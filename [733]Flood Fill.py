# An image is represented by an m x n integer grid image where image[i][j] 
# represents the pixel value of the image. 
# 
#  You are also given three integers sr, sc, and newColor. You should perform a 
# flood fill on the image starting from the pixel image[sr][sc]. 
# 
#  To perform a flood fill, consider the starting pixel, plus any pixels 
# connected 4-directionally to the starting pixel of the same color as the starting 
# pixel, plus any pixels connected 4-directionally to those pixels (also with the same 
# color), and so on. Replace the color of all of the aforementioned pixels with 
# newColor. 
# 
#  Return the modified image after performing the flood fill. 
# 
#  
#  Example 1: 
# 
#  
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.
# e., the red pixel), all pixels connected by a path of the same color as the 
# starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally 
# connected to the starting pixel.
#  
# 
#  Example 2: 
# 
#  
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
# Output: [[2,2,2],[2,2,2]]
#  
# 
#  
#  Constraints: 
# 
#  
#  m == image.length 
#  n == image[i].length 
#  1 <= m, n <= 50 
#  0 <= image[i][j], newColor < 2¹⁶ 
#  0 <= sr < m 
#  0 <= sc < n 
#  
#  Related Topics Array Depth-First Search Breadth-First Search Matrix 👍 3857 ?
# ? 367


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if old_color == newColor:
            return image

        m = len(image)
        n = len(image[0])

        def depth_first_search(i, j) -> None:
            if image[i][j] == old_color:
                image[i][j] = newColor
                if i >= 1:
                    depth_first_search(i - 1, j)
                if i + 1 < m:
                    depth_first_search(i + 1, j)
                if j >= 1:
                    depth_first_search(i, j - 1)
                if j + 1 < n:
                    depth_first_search(i, j + 1)

        depth_first_search(sr, sc)
        return image
# leetcode submit region end(Prohibit modification and deletion)
