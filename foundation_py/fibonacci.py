def fibonacci(self, K):
    """
    input: int K
    return: int
    """
    if K <= 0:
        return 0
    if K == 1:
        return 1
    return self.fibonacci (K - 1) +  self.fibonacci (K - 2)



def factorial(n):
    """
    input: int n
    return: long
    """
    # write your solution here
    # base case
    if n == 1:
        return 1
    # subproblem
    subproblemResult = factorial(n - 1)
    # recursion rule
    return subproblemResult * n 

# print(factorial(5))

class Solution(object):
  def power(self, a, b):
    """
    input: int a, int b
    return: long
    """
    # write your solution here
    # corner case
    if b == 0:
      return 1
    # base case
    if b == 1:
      return a
    # subproblem
    subproblemResult = self.power(a, b/2)
    # recursion rule
    if b % 2 == 0:
       return subproblemResult * subproblemResult
    return subproblemResult * subproblemResult * a

obj = Solution()
x = obj.power(10,3)
print(x)