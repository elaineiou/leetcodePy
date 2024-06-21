class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Creator:
    def populate(self, in_list):
        # creating the head node
        curr = ListNode(in_list[0])
        head = curr
        # iterating over input list
        for i in in_list[1:]:
          temp = ListNode(i)
          curr.next = temp
          curr = temp

        return head


# Below the manual approach for a list of four elements/nodes
# manual_list = ListNode(1)
# manual_list.next = ListNode(2)
# manual_list.next.next = ListNode(3)
# manual_list.next.next.next = ListNode(4)

inputs = [1,2,3,4]
result = Creator().populate(inputs)
