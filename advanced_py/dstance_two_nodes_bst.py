from data_structure.TreeNode import TreeNode


"""
            15
        /       \
        5       20
        /\
        3   10
        /\   /
        1 4  8
            /\
            7  9
"""
class Solution(object):
    def distance_between(self, root, p, q):
        if root == None :
            return -1
        if root.val == p:
            return self.distance_from_root(root, q)
        elif root.val == q:
            return self.distance_from_root(root, p)

        if p > q :
            return self.distance_between(q, p)
        else:
            while root != None:
                if root.val >= p and root.val <= q:
                    return self.distance_from_root(root, p) + self.distance_from_root(root, q)
                elif root.val > q:
                    root = root.left
                else:
                    root = root.right

    def distance_from_root(self, root, target):
        distance = 0
        if root.val == target:
            return distance
        while(root.val != target):
            if root.val > target:
                root = root.left
            else:
                root = root.right
            distance += 1
        return distance




# test
obj = Solution()
root = TreeNode(15)
root.left = TreeNode(5)
root.right = TreeNode(20)
res = obj.distance_between(root,5,20)
print(res)
