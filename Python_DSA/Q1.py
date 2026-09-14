class Solution:

    def count_digit(self,n):
        if n==0:
            return 1
        cnt=0
        while n>0:
            cnt+=1
            n=n//10

        return cnt
    
n =6678

sol=Solution()
ans= sol.count_digit(n)

print(f"The count of digit is {ans}")

