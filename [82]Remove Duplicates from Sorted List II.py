# Given the head of a sorted linked list, delete all nodes that have duplicate 
# numbers, leaving only distinct numbers from the original list. Return the linked 
# list sorted as well. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,1,1,2,3]
# Output: [2,3]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 300]. 
#  -100 <= Node.val <= 100 
#  The list is guaranteed to be sorted in ascending order. 
#  
#  Related Topics Linked List Two Pointers 👍 5520 👎 161


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        pre_result = ListNode()
        result = pre_result

        values_to_drop = set()
        prev_value = None
        while first:
            if prev_value == first.val:
                values_to_drop.add(first.val)
            else:
                prev_value = first.val
            first = first.next

        while head:
            if head.val not in values_to_drop:
                pre_result.next = ListNode(head.val)
                pre_result = pre_result.next
            head = head.next
        return result.next
# leetcode submit region end(Prohibit modification and deletion)
