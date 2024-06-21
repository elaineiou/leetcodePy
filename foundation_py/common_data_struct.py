class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# def print_linked_list(node):
#     res = ""
#     while node != None:
#         val = node.val
#         res = res + val + "--->"
#         node = node.next

#     res = res + "None"