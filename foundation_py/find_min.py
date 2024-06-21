class Solution(object):
  def min(self, array):
    """
    input: int[] array
    return: int
    """
    # write your solution here
    if (array == None):
       return -1
    if (len(array) == 0):
        return 0
    min = array[0]
    for a in array:
        if a < min:
            min = a
    return min
