from data_structure.TreeNode import TreeNode
class Solution:
  def isBalanced(self, root):
    if (root == None):
      return True
    return self.getHeight(root) != -1
  #  input: root
  #  output: height or -1 (not balanced)
  def getHeight(self, root):
    # basecase
    if (root == None):
      return 0

    # recursive rule
    left = self.getHeight(root.left)
    right = self.getHeight(root.right)
    if (left == -1):
      return -1
    if (right == -1):
      return -1
    if abs(left - right) > 1:
      return -1
    return max(left, right) + 1


first = TreeNode(1)
first.left = TreeNode(2)
first.right = TreeNode(3)

obj = Solution()
print (obj.isBalanced(first))
