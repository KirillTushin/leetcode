# Given the head of a linked list, remove the nᵗʰ node from the end of the list 
# and return its head. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1], n = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is sz. 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
#  Follow up: Could you do this in one pass? 
#  Related Topics Linked List Two Pointers 👍 9259 👎 437


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_for_remove = head
        head_for_return = head

        length = 0
        while head:
            length += 1
            head = head.next

        if length == n:
            head_for_return = head_for_return.next
            return head_for_return

        for _ in range(length - n):
            prev = head_for_remove
            head_for_remove = head_for_remove.next
            next = head_for_remove.next

        prev.next = next
        return head_for_return
# leetcode submit region end(Prohibit modification and deletion)
