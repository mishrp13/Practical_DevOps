import math
class Solution:

    def isPerfect(self,n):

        if n==1:
            return False
        
        sum=0

        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                sum=sum+i

            if n//i!=n and i!=n//i:
                sum = sum + (n//i)

        if sum==n:
            return True
        return False


sol=Solution()
n=int(input("enter any number: "))
ans= sol.isPerfect(n)
if ans:
    print(f"{n} is a perfect number: ")
else:
    print(f"{n} is not a perfect number: ")