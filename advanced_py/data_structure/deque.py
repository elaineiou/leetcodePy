# https://www.geeksforgeeks.org/deque-in-python/?ref=ml_lbp
from collections import deque
from TreeNode import TreeNode

d = deque([1,2,3,4,5,6])
res = d.pop()
print(res)
res = d.popleft()
print(d)
print(len(d))
d.append('tmd')
print(d)
d.appendleft(-1)
print(d)

# 把deque当queue用(FIFO)的两个API:
# 1. append() -- 右进
# 2. popleft() -- 左出

"""
deque 模拟 stack
"""
stack = deque()
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
stack.pop()
print(stack)


"""
deque initialize a tree
"""
x = TreeNode(10)
d = deque([x])
print(d)
