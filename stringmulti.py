#! /usr/bin/python
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        l1=len(num1)
        l2=len(num2)
        i=l1/2
        j=l2/2
        if not num1 or not num2: return ''
        if l1==1 and l2==1:
            d1=int(num1[0])
            d2=int(num2[0])
            d=d1*d2
            return str(d)
            
        num1left=num1[:i]
        num1right=num1[i:]
        num2left=num2[:j]
        num2right=num2[j:]
        s1=self.multiply(num1left,num2left)
        s2=self.multiply(num1left,num2right)
        s3=self.multiply(num1right,num2left)
        s4=self.multiply(num1right,num2right)
        for k in range(l1+l2-i-j):
            s1+='0'
        for k in range(l1-i):
            s2+='0'
        for k in range(l2-j):
            s3+='0'
        s5=self.add(s1,s2)
        s6=self.add(s3,s4)
        s7=self.add(s5,s6)
        return s7
        
    def add(self,num1,num2):
        num1=num1[::-1]
        num2=num2[::-1]
        num3=''
        l1=len(num1)
        l2=len(num2)
        l= l1 if l1<l2 else l2
        carry=0
        for i in range(l):
            d1=int(num1[i])
            d2=int(num2[i])
            d=d1+d2+carry
            if d>=10:
                carry=1
                d=d-10
            else:
                carry=0
            nd=str(d)
            num3+=nd
        if l1>l2:
            for i in range(l,l1):
                d1=int(num1[i])
                d=d1+carry
                if d>=10:
                    carry=1
                    d=d-10
                else:
                    carry=0
                nd=str(d)
                num3+=nd
        else:
            for i in range(l,l2):
                d2=int(num2[i])
                d=d2+carry
                if d>=10:
                    carry=1
                    d=d-10
                else:
                    carry=0
                nd=str(d)
                num3+=nd
        if carry: num3+='1'
        num3=num3[::-1]
        return num3
