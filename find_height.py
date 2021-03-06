"""
The height of a binary tree is the number of edges between the tree's root and
its furthest leaf. This means that a tree containing a single node has a height
of 0.

Complete the getHeight function provided in your editor so that it returns the
height of a binary tree. This function has a parameter, root, which is a pointer
to the root node of a binary tree.
Note -The Height of binary tree with single node is taken as zero.

Input Format
You do not need to read any input from stdin. Our grader will pass the root node
of a binary tree to your getHeight function.

Output Format
Your function should return a single integer denoting the height of the binary
tree.

"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def height(root):
    if not root or (not root.left and not root.right):
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))
