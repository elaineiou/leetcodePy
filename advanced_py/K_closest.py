class Solution(object):
  def kClosest(self, array, target, k):
    """
    input: int[] array, int target, int k
    return: int[]
    """
    left = self.findClosest(array, target)
    right = left + 1

    result = [None]*k
    for i in range(k):
      if (right >= len(array)):
        result[i] = array[left]
        left -= 1
      elif abs(array[left] - target) <= abs(array[right] - target):
        result[i] = array[left]
        left -= 1
      else:
        result[i] = array[right]
        right += 1

    return result

  def findClosest(self, array, target):
    left = 0
    right = len(array) - 1
    while (left < right - 1):
      mid = left + (right - left) // 2
      if (array[mid] == target):
        return mid
      elif (array[mid] > target):
        right = mid
      else:
        left = mid
    if abs(array[left] - target) <= abs(array[right] - target):
      return left
    else:
      return right

obj = Solution()
array = [1,5,10,12,13]
print(obj.kClosest(array, 9, 1))
