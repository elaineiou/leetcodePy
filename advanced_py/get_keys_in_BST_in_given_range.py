from data_structure.TreeNode import TreeNode
class Solution(object):
  def getRange(self, root, min, max):
    """
    input: TreeNode root, int min, int max
    return: Integer[]
    """
    # write your solution here
    res = []
    self.helper(root, res, min, max)
    response = res.sort()
    print(response)
    return response

  def helper(self, root, res, min, max):
    # base case
    if root == None:
      return
    if root.val >= min and root.val <= max:
      res.append(root.val)
    # sub problem
    if root.val > min:
      self.helper(root.left, res, min, max)
    if root.val < max:
      self.helper(root.right, res, min, max)

sol = Solution()
res = sol.getRange(None, -1, 0)
