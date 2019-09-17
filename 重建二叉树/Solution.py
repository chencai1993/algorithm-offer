# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
            return None
        root = TreeNode(pre[0])
        ll = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:ll+1],tin[:ll])
        root.right = self.reConstructBinaryTree(pre[ll+1:],tin[ll+1:])
        return root