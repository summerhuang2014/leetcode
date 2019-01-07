'''任务内容
题目1 正则表达式匹配

给定一个字符串 (s) 和一个字符模式 §。实现支持 ‘.’ 和 ‘*’ 的正则表达式匹配。’.’ 匹配任意单个字符，’*’ 匹配零个或多个前面的元素。匹配应该覆盖整个字符串 (s) ，而不是部分字符串。

任务时间
一天'''

#https://leetcode-cn.com/problems/regular-expression-matching/
#评论区找的答案。学习了。https://docs.python.org/3/library/re.html
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        value = re.match(p, s)
        if value == None or value.group(0) != s:
            return False
        else:
            return True