import PrintLL
import ListNodeFactory
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
  def partition(self, head, target):
    """
    input: ListNode head, int target
    return: ListNode
    """
    # write your solution here
    # corner case
    if (head == None or head.next == None):
      return head

    small = ListNode(-1)
    large = ListNode(-1)
    curSmall = small
    curLarge = large
    while (head != None):
      if (head.val < target):
        curSmall.next = head
        curSmall = curSmall.next
      else:
        curLarge.next = head
        curLarge = curLarge.next
      head = head.next

    # post-processing
    curLarge.next = None # de-link to prevent "ListNode contains cycle"
    curSmall.next = large.next
    return small.next

obj = Solution()
array = [3,2,1]
ll = ListNodeFactory.Creator().populate(array)
res = obj.partition(ll, 2)
PrintLL.PrintLL.print(res)
