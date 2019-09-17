class Solution:
    def jumpFloor(self, number):
        # write code here
        a,b=1,1
        if number<=1:
            return number
        for i in range(2,number+1):
            b=a+b
            a=b-a
        return b