#https://leetcode-cn.com/problems/two-sum/
#题目1：两数之和
#描述
#给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
'''题目2：两数相加
描述
给出两个非空的链表用来表示两个非负的整数。其中,它们各自的位数是按照逆序的方式存储的,并且它们的每个节点只能存储一位数字。
题目3：无重复字符的最长子串
描述
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。'''

#no 1, 与官方题解的暴力法相同
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, value in enumerate(nums):
            m = target - value
            if m in nums[i+1:]: 
                nums[i] = -999
                t = ([i, nums.index(m)])
                return(t)
                break


#no 2，在评论区找到的答案
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r=re
        carry=0
        while(l1 or l2):
            x= l1.val if l1 else 0 #如果l1非空，取出储存的数值
            y= l2.val if l2 else 0
            s=carry+x+y
            carry=s//10 #s除以10求整数部分，看是否需要进位
            r.next=ListNode(s%10) #s除以10求余数，存入数据结构中
            r=r.next
            if(l1!=None):l1=l1.next
            if(l2!=None):l2=l2.next
        if(carry>0):
            r.next=ListNode(1) #往下走，储存下一个数字
        return re.next

#no 3，尝试了很久，仍旧报错。看评论区答案的模仿写的。
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        maxlength = 0
        temp = ''

        for i in s:
            if i not in temp:
                temp += i
                length += 1
            else:
                if length >= maxlength:
                    maxlength = length
                ind = temp.index(i) #关键在于遇到重复的值的时候，从原来不重复的子字符串中的重复的值的下一个开始
                temp = temp[(ind+1):] + i
                length = len(temp)
        if length > maxlength: #循环结束，再验证一次。因为到最后一个i的时候会一直到结束都没重复的。需要重新比较一下长度和历史长度
            maxlength = length
        return(maxlength)
        