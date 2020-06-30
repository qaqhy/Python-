"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

案例 1:
输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True

案例 2:
输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 哈希方法
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def func(root):
            if root is None:
                return []
            return func(root.left) + [root.val] + func(root.right)

        ls = func(root)
        if len(ls) < 2:
            return False
        if ls[0] + ls[1] > k or ls[-1] + ls[-2] < k:
            return False
        temp = {}
        for i, ks in enumerate(ls):
            key = k - ks
            if temp.get(key) is not None:
                return True
            temp[ks] = i
        return False


# 双指针方法
class Solution2:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def func(root):
            if root is None:
                return []
            return func(root.left) + [root.val] + func(root.right)

        ls = func(root)
        n = len(ls)
        if n < 2:
            return False
        if ls[0] + ls[1] > k or ls[-1] + ls[-2] < k:
            return False
        L = 0
        R = n - 1
        while L < R:
            if ls[L] + ls[R] == k:
                return True
            elif ls[L] + ls[R] < k:
                L += 1
            else:
                R -= 1
        return False


# 哈希加遍历
class Solution3:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        ans = False
        ds = set()

        def func(root):
            nonlocal ans
            if root is not None and not ans:
                if root.val in ds:
                    ans = True
                    return
                ds.add(k - root.val)
                func(root.left)
                func(root.right)

        func(root)
        return ans
