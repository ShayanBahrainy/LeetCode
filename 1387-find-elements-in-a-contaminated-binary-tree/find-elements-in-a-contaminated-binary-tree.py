# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.values = set()
        self.values.add(0)
        dq = deque()
        dq.appendleft(root)
        while dq:
            node = dq.popleft()
            if node.left:
                dq.appendleft(node.left)
                leftval = (2 * node.val) + 1
                self.values.add(leftval)
                node.left.val = leftval
            if node.right:
                dq.appendleft(node.right)
                rightval = (2 * node.val) + 2
                self.values.add(rightval)
                node.right.val = rightval
    def find(self, target: int) -> bool:
        return target in self.values


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)