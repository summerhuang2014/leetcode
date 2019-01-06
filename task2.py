'''
题目1：寻找两个有序数组的中位数

描述
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
题目2：最长回文子串

描述
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
题目3：字形变换

描述
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
--------------------- 
作者：Datawhale 
来源：CSDN 
原文：https://blog.csdn.net/datawhale/article/details/85266740 
版权声明：本文为博主原创文章，转载请附上博文链接！

'''

#no 1:错误在于除以2而非2.0以及除以1而非1.0。看了参考答案改过来了。
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        y = nums1 + nums2
        y.sort()
        t = len(y)
        if t%2 == 0:
            k = (y[t/2] + y[(t/2)-1])/2.0
        else:
            k = y[(t-1)/2]/1.0
        return(k)
        


#no 2, 5. Longest Palindromic Substring
#https://leetcode-cn.com/problems/longest-palindromic-substring/
#想了很久，看答案的。尝试过暴力法，但代码没实现，迭代错误。原先想法是找到重复出现的字符，找到出现在字符的首个和末个，如出现不符则找反向第二末个
#写之前，在脑袋里动画想象一下解题是怎样的。用最简单、思路最清晰的写。代码写不出来有时候是脑子思路不清晰。
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = "" #s="aaa"
        for i in range(2*len(s)-1):#eg, len(s) == 3, i == 0, 1, 2
            if i%2 == 0:#i == 0; i==2
                start = end = i//2 #start == end == 0; i==2, s=e=1
                while start>=0 and end<len(s) and s[start]==s[end]:#s[0]==s[0]; s[1]==s[1], s[0]==s[1]
                    start-=1 #s[-1]; s[0], s[-1]
                    end+=1#s[1]; s[2], s[3]
            else:#i == 1
                start = (i-1) // 2# start=0,
                end = (i+1) //2# end=1, 
                while start>=0 and end<len(s) and s[start]==s[end]:#s[0]==s[1]
                    start-=1#s[-1]
                    end+=1#s[2]
            if len(str)<=(end-start-1):#i==0, len(str)==0, 1-(-1)-1==1; i==1, 2-(-1)-1=2; i==3, 2<=3-(-1)-1=3
                str=s[start+1:end]#i == 0, str = s[0:1] = s[0]; i==1, str == s[0:2]; i==3, str=s[0:3]
        return str


#no 3, https://leetcode-cn.com/problems/zigzag-conversion/
#还是思路不清晰。参考官方答案的C写的python。如果一下子做不出来，用小的例子来试，逐步增加难度。
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return(s)
        elif s and numRows == 1:
            return(s)
        else:
            s = list(s)
            row = []
            for i in range(numRows):
                row.append(i)
                row[i] = []
            r = 0
            godown = True
            for items in s:
                if r < numRows and godown:
                    row[r] += items
                    r += 1
                    if r == numRows -1:
                        godown = False
                elif r>0 and not godown:
                    row[r] += items
                    r -= 1
                    if r == 0:
                        godown = True
            final = row[0]
            for i in range(1,numRows):
                final += row[i]
            return(''.join(final))