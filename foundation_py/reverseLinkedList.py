import common_data_struct

class Solution(object):
    def reverse(self, head):
        """
        input: ListNode head
        return: ListNode
        """
        # print(head.val)
        # write your solution here
        if head == None or head.next == None:
            return head
        cur = head
        prev = None
        while (cur != None):
            # create a next variable to record cur.next
            next = cur.next
            # reverse the cur.next to prev
            cur.next = prev
            # move prev and cur
            prev = cur
            cur = next
        return prev

node = common_data_struct.ListNode(1)
node2 = common_data_struct.ListNode(2)
node.next = node2
sol = Solution()
res = sol.reverse(node)
print(res.val)
