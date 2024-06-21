"""
True Case:
                ALICE
                /
                ERIC
                /
                CHALES
                /
                SOPHIA

Backtracking called with index=1 and names=['ALICE', 'CHALES', 'ERIC', 'SOPHIA']
Swapped names: ['ALICE', 'ERIC', 'CHALES', 'SOPHIA'], index=1, i=2
Backtracking called with index=2 and names=['ALICE', 'ERIC', 'CHALES', 'SOPHIA']
Swapped names: ['ALICE', 'ERIC', 'CHALES', 'SOPHIA'], index=2, i=2
Backtracking called with index=3 and names=['ALICE', 'ERIC', 'CHALES', 'SOPHIA']
Swapped names: ['ALICE', 'ERIC', 'CHALES', 'SOPHIA'], index=3, i=3
Backtracking called with index=4 and names=['ALICE', 'ERIC', 'CHALES', 'SOPHIA']
Checking last element: SOPHIA and first element: ALICE: True
True
"""

"""
False Case:
                ALICE
                /
                ERIC
                /
                CHALES
                /
                QUEEN

Backtracking called with index=1 and names=['ALICE', 'CHALES', 'ERIC', 'QUEEN']
Swapped names: ['ALICE', 'ERIC', 'CHALES', 'QUEEN'], index=1, i=2
Backtracking called with index=2 and names=['ALICE', 'ERIC', 'CHALES', 'QUEEN']
Swapped names: ['ALICE', 'ERIC', 'CHALES', 'QUEEN'], index=2, i=2
Backtracking called with index=3 and names=['ALICE', 'ERIC', 'CHALES', 'QUEEN']
Restored names: ['ALICE', 'ERIC', 'CHALES', 'QUEEN'], index=2, i=2
Restored names: ['ALICE', 'CHALES', 'ERIC', 'QUEEN'], index=1, i=2
False
"""


class Solution(object):
  def canChain(self, names):
    """
    Example

    Input: String[] = {“ALICE”, “CHARLES”, “ERIC”, “SOPHIA”}

    Output: true
    """
    if (names is None or len(names) == 0):
      return False
    if (len(names) == 1 and self.check(names[0], names[0])):
      return True
    return self.backTracking(names, 1)

  # check if the last char of the former string is equiv to the start char of the latter string
  def check(self, former, latter):
    return former[-1] == latter[0]

  # path: a list to record states
  # index: of the level
  def backTracking(self, names, index):
    print(f"Backtracking called with index={index} and names={names}")

    # base case
    if (index == len(names)):
       result = self.check(names[len(names) - 1], names[0]) # check the last case
       print(f"Checking last element: {names[-1]} and first element: {names[0]}: {result}")
       return result
    for i in range (index, len(names)):
        if(self.check(names[index - 1], names[i])):
            print(f"Before swapped names: {names}, index={index}, i={i}")
            # 当index - 1发现可以和i做同桌后，把i和邻座对调
            self.swap(names, index, i)
            print(f"After swapped names: {names}, index={index}, i={i}")
            # 只有True了才可以继续Stack/Recursion
            if self.backTracking(names, index + 1):
                return True
            # 另一个branch, 如果index - 1发现和i做同桌后，后面的人怎么都坐不对（无法形成infinite loop), 就再次换回来
            # 也可以理解成为一个restore, in case there're other cases of permutations that will actually make a infinite loop!
            else:
                self.swap(names, index, i)
                print(f"Restored names: {names}, index={index}, i={i}")
    return False

  def swap(self, names, i, j):
    names[i], names[j] = names[j], names[i]


# test
obj = Solution()
res = obj.canChain(["ALICE", "CHALES", "ERIC", "SOPHIA"])
print(res)
