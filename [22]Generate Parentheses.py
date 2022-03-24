# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses. 
# 
#  
#  Example 1: 
#  Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#  Example 2: 
#  Input: n = 1
# Output: ["()"]
#  
#  
#  Constraints: 
# 
#  
#  1 <= n <= 8 
#  
#  Related Topics String Dynamic Programming Backtracking 👍 12115 👎 474

# leetcode submit region begin(Prohibit modification and deletion)

def generate(now, left, right, n, combinations):
    if left < n:
        generate(now + '(', left + 1, right, n, combinations)
    if right < left:
        generate(now + ')', left, right + 1, n, combinations)
    if left == right == n:
        combinations.append(now)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = []
        generate('', 0, 0, n, combinations)
        return combinations
# leetcode submit region end(Prohibit modification and deletion)
