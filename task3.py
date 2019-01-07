'''
任务内容
题目1：整数反转

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

题目2：字符串转换整数

请你来实现一个 函数，使其能将字符串转换成整数。

题目3：回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

任务时间
两天
--------------------- 
作者：Datawhale 
来源：CSDN 
原文：https://blog.csdn.net/datawhale/article/details/85266834 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

#no 1, https://blog.csdn.net/datawhale/article/details/85266834
#不难，考虑到题目的特殊例子就好
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        init = []
        if x < 0:
            t = -1
        else:
            t = 1
        x = abs(x)
        while x > 0.5:
            a = x%10
            init.append(a)
            x = int(x/10)
        answer = 0
        for num in init:
            answer *= 10
            answer += num
        if -2**31 < answer < 2**31-1:
            return(answer*t)
        else:
            return(0)
        

#no 2，自己的答案，仍然有例子不让过。
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str and bool(str.strip()):
            str.strip()
            t = str.split()[0]
            if t[0] == '-' and t[1:].isdigit():
                ans = (-1)*int(t[1:])
            elif t[0] == '+' and t[1:].isdigit():
                ans = int(t[1:])
            elif t.isdigit():
                ans = int(t)
            elif t.replace('.','',1).isdigit():
                ans = int(float(t))
            else:
                ans = 0
            if -2**31 < ans < 2**31 -1:
                return(ans)
            elif ans > 2**31:
                return(2**31-1)    
            elif ans < -2**31:
                return(-2**31)
        else:
            return(0)

#评论区的答案。思路很简洁清晰，没有奇怪/太新颖的构想。编程是逻辑的实现，逻辑正确是第一步。
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        coll=''
        str=str.strip()#去头去尾
        t=len(str)

        for i in range(t):
            #是数字吗？
            if str[i]>='0' and str[i]<='9':
                coll+=str[i]
                if i==t-1 or str[i+1]<'0' or str[i+1]>'9':#如果到末位或者下一位与之前的不能做出正常数字
                    out=int(coll)
                    if out<-2**31:
                        return -2**31
                    elif out>2**31-1:
                        return 2**31-1
                    else:
                        return int(out)
            #是正号或负号吗？
            elif str[i]=='-' or str[i]=='+':
                if i<t-1 and str[i+1]>='0' and str[i+1]<='9':#如果没到末位且下一位能正常形成数字
                    coll+=str[i]
                else:
                    return 0
            else:
                return 0
        return 0

#no 3, https://leetcode-cn.com/problems/palindrome-number/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0:
            y = str(x)
            t = ''.join(reversed(y))
            if int(t) == x:
                return(bool(t))
            else:
                return(not bool(x))
        else:
            return(not bool(x))