#! /usr/bin/python
#################
# This module is to detect whether the input string is a repeatition
# of a substring with length larger than 2, and return a boolean value
#################

class Solution:
   '''This is the doc string for solution class'''
   def repeat(self,s):
      '''This method detect whether the string is a repeatition'''
      n=len(s)
      f=self.factor(n)
      if not f :
         return False
      else:
         for i in range(0,n):
            if s[0]==s[i]:
               pass
            else:
               break
         else:
            return False
         for fac in f:
            for i in range(0,n,fac):
		if s[0:fac]==s[i:i+fac] :
		    pass
                else:
                    break
            else:
                return True
         return False 

   def factor(self,n):
      ''' This method calculate the factors of a non-prime number and return
          a list'''
      flist=[]
      if n<=2:
         return flist
      else:
         for i in range(2,n/2+1):
             if n%i==0: flist.append(i)
         return flist

