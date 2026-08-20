class Solution:

    def Pattern2(self,n):

        for i in range(n):
            for j in range(i+1):
                print(j+1,end="")

            print()


    def main(self):
        N=5
        sol=Solution()
        sol.Pattern2(N)


if __name__=="__main__":
    Solution().main()