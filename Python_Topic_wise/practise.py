class Solution:

    def maxOccurence(self,nums):

        n= len(nums)

        maxele=0
        maxfreq=0

        visited= [False]*n

        for i in range(n):
            if visited[i]:
                continue


            freq=0

            for j in range(i,n):
                if nums[i]==nums[j]:
                    freq+=1
                    visited[j]=True

            if freq> maxfreq:
                maxfreq=freq
                maxele=nums[i]
            elif freq==maxfreq:
                maxele=min(maxele,nums[i])
            
        

        return maxele


if __name__=="__main__":
    nums= [1,2,2,3,4,4,4,4,5]
    sol=Solution()
    ans=sol.maxOccurence(nums)
    print(f"{ans}")
        