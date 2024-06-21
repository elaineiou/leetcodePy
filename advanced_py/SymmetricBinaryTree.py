from data_structure.TreeNode import TreeNode

class Solution(object):
  def isSymmetric(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    if (root == None):
      return True
    return self.isSymmetricHelper(root.left, root.right)

  def isSymmetricHelper (self, left, right):
    if (left == None and right == None):
      return True
    elif (left == None or right == None):
      return False
    elif (left.val != right.val):
      return False
    return self.isSymmetric(left.left, right.right) and self.isSymmetric(left.right, right.left)

node = TreeNode(1)

obj = Solution()
obj.isSymmetric(node)
