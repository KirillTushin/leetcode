# You are given the heads of two sorted linked lists list1 and list2. 
# 
#  Merge the two lists in a one sorted list. The list should be made by 
# splicing together the nodes of the first two lists. 
# 
#  Return the head of the merged linked list. 
# 
#  
#  Example 1: 
# 
#  
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#  
# 
#  Example 2: 
# 
#  
# Input: list1 = [], list2 = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: list1 = [], list2 = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both lists is in the range [0, 50]. 
#  -100 <= Node.val <= 100 
#  Both list1 and list2 are sorted in non-decreasing order. 
#  
#  Related Topics Linked List Recursion 👍 11488 👎 1038


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def insert(pointer, list_node):
    pointer.next = ListNode(list_node.val)
    pointer = pointer.next
    list_node = list_node.next
    return pointer, list_node


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer = ListNode()
        head = pointer

        while list2 and list1:
            if list1.val < list2.val:
                pointer, list1 = insert(pointer, list1)
            else:
                pointer, list2 = insert(pointer, list2)

        while list1:
            pointer, list1 = insert(pointer, list1)

        while list2:
            pointer, list2 = insert(pointer, list2)

        return head.next
# leetcode submit region end(Prohibit modification and deletion)