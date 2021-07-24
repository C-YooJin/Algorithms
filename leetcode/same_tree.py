"""
[leetcode] 100. SameTree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p is None and q is None:      # 만약 두 값이 둘 다 None이면 True
            return True
        
        if p.val != q.val:      # 두 값이 다르면 False
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# TODO: Test case 1
# if __name__ == "__main__":
#     q = TreeNode(1)
#     q.left = TreeNode(2)
#     q.right = TreeNode(3)
#     p = TreeNode(1)
#     p.left = TreeNode(2)
#     p.right = TreeNode(3)


# TODO: Test Case 2
# if __name__ == "__main__":
#     q = TreeNode(1)
#     q.left = TreeNode(2)
#     p = TreeNode(1)
#     p.left = TreeNode(None)
#     p.right = TreeNode(2)

# TODO: Test Case 3
if __name__ == "__main__":
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(1)
    p = TreeNode(1)
    p.left = TreeNode(1)
    p.right = TreeNode(2)

solution = Solution()
print(solution.isSameTree(p, q))