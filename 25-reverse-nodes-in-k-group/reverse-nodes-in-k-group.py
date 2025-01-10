# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        final_array = []
        stack = []
        while node:
            if len(stack) == k:
                i = len(stack) - 1
                while i >= 0:
                    final_array.append(stack[i])
                    i -= 1
                stack = []
                stack.append(node.val)
            else:
                stack.append(node.val)

            node = node.next
        if len(stack) != k:
            i = 0
            while i < len(stack):
                final_array.append(stack[i])
                i += 1
        if len(stack) == k:
            i = len(stack) - 1
            while i >= 0:
                final_array.append(stack[i])
                i -= 1
        head = ListNode(final_array[0])
        last = head
        for i in range(1,len(final_array)):
            last.next = ListNode(final_array[i])
            last = last.next
        return head


