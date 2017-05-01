"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def inOrder(root):
    if root is None:
        return
    if root.left is not None:
        inOrder(root.left)
    print(root.data, end=' ')
    if root.right is not None:
        inOrder(root.right)
