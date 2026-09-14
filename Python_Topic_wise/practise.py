class Solution:

    def largest_num(self,n):

        largest=0

        while n >0:
            last_digit= n%10
            if last_digit > largest:
                largest=last_digit
            n=n//10

        return largest


n=12568249
sol=Solution()
ans=sol.largest_num(n)
print(f"{ans}")
