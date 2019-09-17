class Solution:
    def cutRope(self, number):
        # write code here
        res = [0,0,1,2,4,6]
        for i in range(6,number+1):
            maxx = 0
            for j in range(3,int(i/2)):
                t = res[j]*res[i-j]
                if t>maxx:
                    maxx=t
            res.append(maxx)
        return res[number]

'''
链接：https://www.nowcoder.com/questionTerminal/57d85990ba5b440ab888fc72b0751bf8?f=discussion
来源：牛客网

动态规划求解问题的四个特征： 
①求一个问题的最优解； 
②整体的问题的最优解是依赖于各个子问题的最优解； 
③小问题之间还有相互重叠的更小的子问题； 
④从上往下分析问题，从下往上求解问题；
贪婪解法： 当n大于等于5时，我们尽可能多的剪长度为3的绳子；当剩下的绳子长度为4时，把绳子剪成两段长度为2的绳子。 为什么选2，3为最小的子问题？因为2，3包含于各个问题中，如果再往下剪得话，乘积就会变小。 为什么选长度为3？因为当n≥5时，3(n−3)≥2(n−2)

'''
