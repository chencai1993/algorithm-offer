# -*- coding:utf-8 -*-
class Solution:

    def dfs(self,i,j,path):

        if i<0 or i>=self.rows or j<0 or j>=self.cols:
            return False
        #print(i,j,path,self.matrix[i][j],self.tmp[i][j])
        if self.matrix[i][j]!=path[0] or self.tmp[i][j]:
            return False
        if len(path)==1 and self.matrix[i][j]==path[0]:
            return True
        self.tmp[i][j]=True
        if self.dfs(i+1,j,path[1:]) or self.dfs(i-1,j,path[1:]) or self.dfs(i,j-1,path[1:]) or self.dfs(i,j+1,path[1:]):
            return True
        self.tmp[i][j]=False
        return False

    def hasPath(self, matrix, rows, cols, path):
        # write code here

        self.matrix = [list(matrix[i*cols:(i+1)*cols]) for i in range(0,rows)]
        self.rows,self.cols = rows,cols
        for i in range(rows):
            for j in range(cols):
                if self.matrix[i][j]==path[0]:
                    self.tmp=[]
                    for p in range(rows):
                        t = []
                        for q in range(cols):
                            t.append(False)
                        self.tmp.append(t)
                    if self.dfs(i,j,path):
                        return True
        return False


print(Solution().hasPath("ABCESFCSADEE",3,4,"ABCCED"))