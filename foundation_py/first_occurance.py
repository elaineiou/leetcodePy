class Solution(object):
  def firstOccur(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    # write your solution here
    # corner case
    if (array == None or len(array) == 0):
      return -1

    left = 0
    right = len(array) - 1
    
    while(left < right - 1):
      mid = left + (right - left) // 2
      if (array[mid] == target):
        right = mid
      elif (array[mid] < target):
        left = mid + 1
      else:
        right = mid - 1

    # post-processing
    if array[left] == target:
      return left
    if array[right] == target:
      return right
    return -1


array = [3, 4, 5, 6, 6, 9, 16]
obj = Solution()
n = obj.firstOccur(array, 6)
print(n)