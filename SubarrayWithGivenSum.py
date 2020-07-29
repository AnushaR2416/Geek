#
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15

** For More Input/Output Examples Use 'Expected Output' option **
#






def SumSubArray(a,N,S):
    sum=0
    start=0
    for i in range(N):
        if(sum+a[i]<=S):
            sum+=a[i]
        else:
            sum+=a[i]
            while(sum>S):
                sum-=a[start]
                start+=1
        if(sum==S):
            print(start+1,i+1)
            return
        if(i==N-1 and sum!=S):
            print("-1")
            return

T=int(input())
while(T>0):
    NS=list(map(int,input().split(" ")))
    N=NS[0]
    S=NS[1]
    a=[int(num) for num in input().split()]
    SumSubArray(a,N,S)
    T-=1
