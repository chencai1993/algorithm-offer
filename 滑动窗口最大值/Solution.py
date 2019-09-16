# -*- coding:utf-8 -*-


'''
解题思路
设置一个双端队列，队头存储当前滑动窗口最大值的下标
遍历整个列表的时候，实际上就是维护这个列表的过程，先检查第一个元素算法还在滑动窗口内部，若不在，则弹出，再从队尾开始依次弹出比当前元素小的下标
最后将当前元素入队


'''
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        queue = []
        res = []
        if size<=0:
            return []
        for i in range(0,len(num)):
            if len(queue)>0 and queue[0]<i-size+1:
                queue.pop(0)
            while len(queue)>0 and num[queue[-1]]<num[i]:
                queue.pop()
            queue.append(i)
            if i>=size-1:
                res.append(num[queue[0]])
        return res
