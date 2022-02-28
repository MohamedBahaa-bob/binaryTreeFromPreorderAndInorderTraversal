# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid + 1:], inorder[:mid:])
        root.right = self.buildTree(preorder[mid + 1::], inorder[mid + 1::])
        return root


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).val)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
