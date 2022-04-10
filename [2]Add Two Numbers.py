# You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order, and each of their nodes contains a 
# single digit. Add the two numbers and return the sum as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the 
# number 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#  
# 
#  Example 2: 
# 
#  
# Input: l1 = [0], l2 = [0]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each linked list is in the range [1, 100]. 
#  0 <= Node.val <= 9 
#  It is guaranteed that the list represents a number that does not have 
# leading zeros. 
#  
#  Related Topics Linked List Math Recursion 👍 17677 👎 3666


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode(0, ListNode(0))
        result = head
        len_result = 0
        while l1 or l2 or carry:
            l1_val = 0
            l2_val = 0

            if l1:
                l1_val = l1.val
                l1 = l1.next
            if l2:
                l2_val = l2.val
                l2 = l2.next

            val = l1_val + l2_val + carry

            carry, val = divmod(val, 10)
            head.next = ListNode(val=val)
            head = head.next
            len_result += 1
        return result.next
# leetcode submit region end(Prohibit modification and deletion)
