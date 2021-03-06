"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def preOrder(root):
    if root is None:
        return
    if root.left is not None:
        preOrder(root.left)
    print(root.data, end=' ')
    if root.right is not None:
        preOrder(root.right)
