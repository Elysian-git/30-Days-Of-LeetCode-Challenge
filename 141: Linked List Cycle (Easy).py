# ------------ O(n) TC ---------- O(1) SC --------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

#  for visualization check here: https://www.finalroundai.com/articles/detect-loop-linked-list
# OR 
# here: https://leetcode.com/problems/linked-list-cycle/solutions/6556606/0ms-100-step-by-step-explained-with-visualization-easiest-to-understand-java-c-python/
