# You are given an array of k linked-lists lists, each linked-list is sorted in 
# ascending order. 
# 
#  Merge all the linked-lists into one sorted linked-list and return it. 
# 
#  
#  Example 1: 
# 
#  
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#  
# 
#  Example 2: 
# 
#  
# Input: lists = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: lists = [[]]
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  k == lists.length 
#  0 <= k <= 10⁴ 
#  0 <= lists[i].length <= 500 
#  -10⁴ <= lists[i][j] <= 10⁴ 
#  lists[i] is sorted in ascending order. 
#  The sum of lists[i].length will not exceed 10⁴. 
#  
#  Related Topics Linked List Divide and Conquer Heap (Priority Queue) Merge 
# Sort 👍 11735 👎 459


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge2lists(left: ListNode, right: ListNode) -> ListNode:
    result = point = ListNode()

    while left and right:
        if left.val > right.val:
            point.next = right
            right = right.next
        else:
            point.next = left
            left = left.next
        point = point.next

    if left:
        point.next = left
    else:
        point.next = right
    return result.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k == 0:
            return None

        while k > 1:
            for i in range(k // 2):
                left = lists[i]
                right = lists.pop(i+1)
                lists[i] = merge2lists(left, right)
            k = len(lists)

        return lists[0]

# leetcode submit region end(Prohibit modification and deletion)
