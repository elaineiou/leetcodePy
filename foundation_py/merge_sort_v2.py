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

  def merge(self, array, left1, right1, left2, right2):
    # create new array
    result = [] # do we really need to create a new space to merge two sorted array?!!    every recursion will take extra space to store it!


    i = left1
    j = left2

    # 谁小取谁，取谁移谁
    while (i <= right1) and (j <= right2):
      if (array[i] < array[j]):
        swap(arr, i, j)
        i += 1
      else:
        swap(arr, i, j)
        j += 1
    
    # append 完剩下的
    while (i <= right1):
      result.append(leftArray[i])
      i += 1
    while (j < len(rightArray)):
      result.append(rightArray[j])
      j += 1
    
    return result

array = [1,5,3,2,4]
sol = Solution()
sol.mergeSort(array)