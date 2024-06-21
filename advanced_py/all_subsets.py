class Solution(object):
  def subSets(self, set):
    """
    input : String set
    return : String[]
    """
    array = list(set)
    index = 0
    res = []
    path = []
    self.dfs(array, index, res, path)
    return res
    # write your solution here
  # array: ['a', 'b', 'c'], list of char
  # index: index of array
  # res: output string[]
  # path: record states, list of char
  def dfs(self, array, index, res, path):
    # base case
    if (index == len(array)):
      res.append("".join(path))
      return
    # recursive rule
    c = array[index]
    ## add
    path.append(c)
    self.dfs(array, index + 1, res, path)
    path.pop()
    ## not add
    self.dfs(array, index + 1, res, path)
