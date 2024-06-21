class Solution(object):
  def smallestElementLargerThanTarget(self, array, target):
    """
    input: int[] array, int target
    return: int
    """
    left = 0
    right = len(array) - 1
    while (left < right - 1):
      mid = left + (right - left)//2
      if (array[mid]<=target):
        left = mid + 1
      else:
        right = mid
    if array[left] > target:
      return left
    if array[right] > target:
      return right
    return left

obj = Solution()
res = obj.smallestElementLargerThanTarget([4,9,12,13,15,20,21,23,25,28,31,33,34,38,40,42,45,46,48,53,54,56,57,58], 6)
print(res)
