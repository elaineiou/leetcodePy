# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
  def selectionSort(self, head):
    """
    input: ListNode head
    return: ListNode
    """
    # write your solution here
    cur = head
    while (cur):
      min = cur
      nxt = cur.next

      # find the min for the unsorted list
      while (nxt):
        if(nxt.val < min.val):
          min = nxt
        nxt = nxt.next

      # swap
      tmp = cur.val
      cur.val = min.val
      min.val = tmp

      cur = cur.next
    return head
