import ListNodeFactory
import PrintLL

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
  def reorder(self, head):
    """
    input: ListNode head
    return: ListNode
    """

    if head == None or head.next == None:
      return head
    mid = self.findMid(head)
    # PrintLL.PrintLL.print(mid)

    one = head
    two = mid.next

    mid.next = None # de-link
    PrintLL.PrintLL.print(head)

    return self.merge(one, self.reverse(two))

  def findMid(self, head):
    slow = head
    fast = head
    while (fast.next != None and fast.next.next != None):
      slow = slow.next
      fast = fast.next.next
    return slow

  def reverse(self, head):
    # base case
    if (head == None or head.next == None):
      return head
    # subproblem
    subproblemNode = self.reverse(head.next)
    # recursive rule
    head.next.next = head
    head.next = None
    return subproblemNode

  def merge(self, one, two):
     dummyNode = ListNode(-1)
     cur = dummyNode

     while (one != None and two != None):
        cur.next = one
        one = one.next
        cur.next.next = two
        two = two.next
        cur = cur.next.next
     # post-processing
     if (one != None):
        cur.next = one
     else:
        cur.next = two
     return dummyNode.next



inputs = [1,2,3,4]
linkedList = ListNodeFactory.Creator().populate(inputs)

obj = Solution()
res = obj.reorder(linkedList)
# PrintLL.PrintLL.print(res)
