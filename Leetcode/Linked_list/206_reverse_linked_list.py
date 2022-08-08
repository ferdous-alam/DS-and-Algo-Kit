# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution 1: recursion ---------------------------------
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None        
        return p
        
        return levels
                

# Complexity: 
    # Time complexity : O(n) Assume that n is the list's length

    # Space complexity : O(n) The extra space comes from implicit stack space due to recursion.


# solution 2: iterative ----------------------------------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        return prev
                        

# Complexity: 
    # Time complexity : O(n) Assume that n is the list's length

    # Space complexity : O(1) 
