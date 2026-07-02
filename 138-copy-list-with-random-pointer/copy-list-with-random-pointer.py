"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # original node -> copied node
        hashmap = {}

        # ----------------------------------
        # Pass 1: Create all copied nodes
        # ----------------------------------
        curr = head

        while curr:
            hashmap[curr] = Node(curr.val)
            curr = curr.next
        # ----------------------------------
        # Pass 2: Connect next and random
        # ----------------------------------
        curr = head

        while curr:

            copy_node = hashmap[curr]

            copy_node.next = hashmap.get(curr.next)
            copy_node.random = hashmap.get(curr.random)

            curr = curr.next

        return hashmap[head]
        