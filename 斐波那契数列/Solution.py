# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        a,b=0,1
        if n<=1:
            return n
        for i in range(2,n+1):
            b=a+b
            a=b-a
        return b