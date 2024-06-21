#              1221
#              /   \
# 0:         A221  X21
#           /  \      /
# 1:      AA21  AX1     ...

# Time complexity: O(branch^level) = O(2**len(input))
# Space complexity: O(len(input))

class Solution(object):
  def decode(self, input):
    """
    Find all possible decode ways.
    input: string input "1221"
    return: string "ABC"
    """
    # write your solution here
    path = []
    # Creating a dictionary with keys from 1 to 26 and values as letters from 'a' to 'z'
    alphabet_map = {i: chr(96 + i) for i in range(1, 27)}
    self.dfs(path, input, 0, alphabet_map)

  # path: a list to record states
  # index: of the level
  def dfs(self, path, input, index, map):
    # base case
    if (index == len(input)):
       print(''.join(path))
       return
    # recursive rule
    # assume input[index] is alwasys a number
    # decode single num digit
    num = int(input[index])
    if num >= 1 and num <= 9:
      path.append(map[num])
      self.dfs(path, input, index + 1, map)
      path.pop()

    # decode double number digits
    if (index + 1 < len(input)):
      num = num*10 + (int(input[index + 1]))
      if num >= 10 and num <= 26:
        path.append(map[num])
        self.dfs(path, input, index + 2, map)
        path.pop()


# test
obj = Solution()
obj.decode("1221")
