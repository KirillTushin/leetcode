# Given the head of a linked list and an integer val, remove all the nodes of 
# the linked list that has Node.val == val, and return the new head. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [], val = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [7,7,7,7], val = 7
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 10⁴]. 
#  1 <= Node.val <= 50 
#  0 <= val <= 50 
#  
#  Related Topics Linked List Recursion 👍 4669 👎 159


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pointer = ListNode()
        result = pointer

        while head:
            if head.val == val:
                head = head.next
                continue
            pointer.next = ListNode(head.val)
            pointer = pointer.next
            head = head.next

        return result.next
# leetcode submit region end(Prohibit modification and deletion)
