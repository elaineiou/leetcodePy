# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def insertNode(head, target):
  """
  input: ListNode head, int target
  return: ListNode
  """
  cur = head
  newNode = ListNode(target)
  
  #  case 2: find the right insert position
  while (cur.next != None and  newNode.val > cur.next.val ):
    cur = cur.next
  # 建立新的链接
  newNode.next = cur.next
  cur.next = newNode
  return head
 
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3) 
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4

n5 = 3.5


insertNode(n1, n5)

a = 1
# print(a)