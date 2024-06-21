class Solution(object):
  def mergeSort(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    if (array == None or len(array) <= 1):
      return array
    left = 0
    right = len(array) - 1
    return self.mergeSortHelper(array, left, right)


  def mergeSortHelper(self, array, left, right):
    # base case
    # 为什么不是len <= 1?
    if (left == right):
      result = []
      result.append(array[left])
      return result

    # subproblem
    mid = left + (right - left)//2 # python 语言特性： //是floor division

    leftArray = self.mergeSortHelper(array, left, mid)
    rightArray = self.mergeSortHelper(array, mid + 1, right)
    # recursion rule
    return self.merge(leftArray, rightArray)

  def merge(self, leftArray, rightArray):
    print("leftArray:", leftArray)
    print("rightArray:", rightArray)

    # create new array
    result = []
    # create indices
    i = 0
    j = 0

    # 谁小取谁，取谁移谁
    while (i < len(leftArray) and j < len(rightArray)):
      if (leftArray[i] < rightArray[j]):
        result.append(leftArray[i])
        i += 1
      else:
        result.append(rightArray[j])
        j += 1
    
    # append 完剩下的
    while (i < len(leftArray)):
      result.append(leftArray[i])
      i += 1
    while (j < len(rightArray)):
      result.append(rightArray[j])
      j += 1
    
    return result

array = [1,5,3,2,4]
sol = Solution()
sol.mergeSort(array)