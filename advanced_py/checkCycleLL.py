# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
  def checkCycle(self, head):
    """
    input: ListNode head
    return: boolean
    """
    if (head == None):
      return False
    slow = head
    fast = head
    while (fast.next != None):
      slow = slow.next
      fast = fast.next.next
      if (fast == slow):
        return True
    return False

