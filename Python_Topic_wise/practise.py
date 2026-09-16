class Solution:

    def reverse_array(self,arr,n):

        p1=0
        p2=n-1


        while p1<p2:

            temp=arr[p1]
            arr[p1]=arr[p2]
            arr[p2]=temp
            p1+=1
            p2-=1

        return 


def printArray(arr,n):

    for i in range(n):
        print(arr[i],end= " ")

    print()


if __name__=="__main__":
    arr= [1,2,3,4,5]
    n=len(arr)
    sol=Solution()
    print(f"Before Reversal")
    printArray(arr,n)
    sol.reverse_array(arr,n)
    print(f"After Reversal: ")
    printArray(arr,n)
    






    