# You are given two lists of closed intervals, firstList and secondList, where 
# firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of 
# intervals is pairwise disjoint and in sorted order. 
# 
#  Return the intersection of these two interval lists. 
# 
#  A closed interval [a, b] (with a <= b) denotes the set of real numbers x 
# with a <= x <= b. 
# 
#  The intersection of two closed intervals is a set of real numbers that are 
# either empty or represented as a closed interval. For example, the intersection 
# of [1, 3] and [2, 4] is [2, 3]. 
# 
#  
#  Example 1: 
# 
#  
# Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],
# [15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#  
# 
#  Example 2: 
# 
#  
# Input: firstList = [[1,3],[5,9]], secondList = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= firstList.length, secondList.length <= 1000 
#  firstList.length + secondList.length >= 1 
#  0 <= starti < endi <= 10⁹ 
#  endi < starti+1 
#  0 <= startj < endj <= 10⁹ 
#  endj < startj+1 
#  
#  Related Topics Array Two Pointers 👍 4052 👎 82


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []

        first_len = len(firstList)
        second_len = len(secondList)

        first_pointer = 0
        second_pointer = 0

        while first_pointer < first_len and second_pointer < second_len:
            first_start, first_end = firstList[first_pointer]
            second_start, second_end = secondList[second_pointer]

            if first_end < second_end:
                if first_end >= second_start:
                    result.append([max(second_start, first_start), first_end])
                first_pointer += 1

            else:
                if second_end >= first_start:
                    result.append([max(second_start, first_start), second_end])
                second_pointer += 1

        return result
# leetcode submit region end(Prohibit modification and deletion)
