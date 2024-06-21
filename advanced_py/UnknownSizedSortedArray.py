# Definition for a unknown sized dictionary.
# class Dictionary(object):
#   def get(self, index):
#     pass

class Solution(object):
  def search(self, dic, target):
    """
    input: Dictionary dic, int target
    return: int
    """
    if (dic == None):
      return -1
    left = 0
    right = 1
    # 快慢指针的思想
    while (dic.get(right) != None and dic.get(right) < target):
      left = right
      right = 2 * right
    return self.binarySearch (dic, target, left, right)
  def binarySearch(self, dic, target, left, right):
    while (left <= right):
      mid = left + (right - left) // 2
      if (dic.get(mid) > target):
        right = mid - 1
      elif (dic.get(mid) == target):
        return mid
      else:
        left = mid + 1
    return -1
