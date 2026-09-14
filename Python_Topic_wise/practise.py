import math
class Solution:


    def is_prime(self,n):

        if n<2:
            return False


        for i in range(2,n):
            if n%i==0:
                return False

        return True

n=17

sol=Solution()
ans= sol.is_prime(n)
print(f"{ans}")