class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows,cols = len(array),len(array[0])
        i,j=0,cols-1
        while i>=0 and i<rows and j>=0 and j<cols:
            t = array[i][j]
            if t==target:
                return True
            elif target<t:
                j-=1
            else:
                i+=1
        return False
