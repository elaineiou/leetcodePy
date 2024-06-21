class Solution(object):
  def permutations(self, input):
    """
    input: string input
    return: string[]
    """
    # write your solution here
    path = list(input)
    res = []
    self.dfs(path, res, len(input), 0)
    return res
  # n: len of the input
  # path: to record states
  # res: result
  # index: of the level
  def dfs(self, path, res, n, index):
    # base case
    if (index == n):
       res.append("".join(path))
       return
    # recursive rule
    for i in range(index, n):
        self.swap(path, i, index)
        self.dfs(path, res, n, index + 1)
        self.swap(path, i, index)


  def swap(self, arr, i, j):
     temp = arr[i]
     arr[i] = arr[j]
     arr[j] = temp
