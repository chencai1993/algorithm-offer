class Solution:
    def init(self,rows,cols):
        self.visited=[[False for j in range(cols)] for i in range(rows)]
        self.res=0
    def movingCount(self, threshold, rows, cols):
        self.init(rows,cols)
        self.threshold,self.rows,self.cols=threshold,rows,cols
        self.dfs(0,0)
        return self.res
    def bitSum(self,i,j):
        i = map(int,list(str(i)))
        j = map(int,list(str(j)))
        return sum(i)+sum(j)
    def dfs(self,i,j):
        if i<0 or j<0 or i>=self.rows or j>=self.cols or self.visited[i][j] or self.bitSum(i,j)>self.threshold:
            return
        self.res+=1
        self.visited[i][j]=True
        self.dfs(i+1,j)
        self.dfs(i-1,j)
        self.dfs(i,j+1)
        self.dfs(i,j-1)


'''
思路：将地图全部置1，遍历能够到达的点，将遍历的点置0并令计数+1.这个思路在找前后左右相连的点很有用，比如leetcode中的海岛个数问题/最大海岛问题都可以用这种方法来求解。
'''