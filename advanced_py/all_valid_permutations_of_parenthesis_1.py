class Solution(object):
  def validParentheses(self, n):
    """
    input: int n
    return: string[]
    """
    # write your solution here
    res = []
    self.dfs([], res, n, 0, 0)
    return res
    # left: count of '('
    # right: count of ')'
    # path: an array to record states in each level
    # res: result
  def dfs(self, path, res, n, left, right):
    # base case
    if (left == n and right == n):
        res.append("".join(path))
        return
    # recursive rule
    ## 左边
    if (left < n):
        path.append('(')
        self.dfs(path, res, n, left + 1, right)
        path.pop()

    ## 右边
    if (left > right):
        path.append(')')
        self.dfs(path, res, n, left, right + 1)
        path.pop()
