# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dq = deque()

        while temp1 and temp2:
            if temp1.val < temp2.val:
                dq.append(temp1.val)
                temp1 = temp1.next
            else:
                dq.append(temp2.val)
                temp2 = temp2.next

        while temp1:
            dq.append(temp1.val)
            temp1 = temp1.next

        while temp2:
            dq.append(temp2.val)
            temp2 = temp2.next

        # Convert deque to linked list
        if not dq:
            return None

        head = ListNode(dq.popleft())
        curr = head

        while dq:
            curr.next = ListNode(dq.popleft())
            curr = curr.next

        return head