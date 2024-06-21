from collections import deque
from data_structure.TreeNode import TreeNode

class Solution(object):
  def rightView(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    # write your solution here
    if not root:
      return []

    d = deque([root])
    rightView = []
    while d:
      size = len(d)
      level = []
      for i in range(size):
        cur = d.popleft()
        level.append(cur.val)
        if cur.left:
          d.append(cur.left)
        if cur.right:
          d.append(cur.right)
      rightView.append(level[-1])
    return rightView

TreeNode.
