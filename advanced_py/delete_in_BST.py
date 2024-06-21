from data_structure.TreeNode import TreeNode

class Solution(object):
  def deleteTree(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # write your solution here

    # base case
    if root == None:
        return None

    # recursive rule
    # case 1
    if root.val == key and root.left == None and root.right == None:
       return None

    # case 2
    if root.val == key and root.left == None and root.right != None:
        return root.right

    # case 3
    if root.val == key and root.left != None and root.right == None:
        return root.left

    # case 4
    if root.val == key:
       smallest = self.succesor(root.right)   # find smallest value larger than key
       root.val = smallest
       root.right = self.deleteTree(root.right, smallest)
       return root

    if root.val < key:
        return self.deleteTree(root.right, key)
    else:
       return self.deleteTree(root.left, key)


  # find smallest val given a tree
  def succesor(self, root):
    while root.left:
        root = root.left
    return root.val
