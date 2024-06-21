# T: O(n), S: O(n)
class Solution(object):
  def reverseWords(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    # 1. convert input str to char array
    c = list(input)
    # 2. reverse char array
    self.reverse(c, 0, len(c) - 1)
    # 3. reverse each word in the char array
    i = 0
    while (i < len(c)):
      j = i
      while (j < len(c) and c[j] != ' '):
        j += 1
      self.reverse(c, i, j - 1)
      i = j + 1
    return "".join(c)

  # c: char array
  def reverse(self, c, i, j):
    while ( i < j):
      # swap
      temp = c[i]
      c[i] = c[j]
      c[j] = temp
      i += 1
      j -= 1
