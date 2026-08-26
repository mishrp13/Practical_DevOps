class Solution():

    def reverse_number(self,n):

        copy=n

        reverse_number=0

        while n>0:

            last_digit= n%10
            reverse_number=(reverse_number*10)+last_digit
            n=n//10

        return reverse_number == copy


n=121
sol=Solution()
ans=sol.reverse_number(n)
print(f"{ans}")





       
       

