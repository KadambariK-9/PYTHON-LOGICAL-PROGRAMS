#ADVANCED CONTIGEUOUS SUBARRAY OF BASKETBALL CONTEST
'''

INPUT
5.......NO OF SHOTS
2........SIZE OF SUBARRAY LIKE [1,2] [2,3] [3,4] [4,5]
1 2 3 4 5.............DISTANCE BASKET TO SHOTS
LOGIC: SCORE=DISTANCE * POSITION.......(POSITION MEANS INDEX OF VALUE)
 OUTPUT
 14.MAX SCORE

 [1,2]
 1*1+2*2=5
 [2,3]
 2*1+3*2=8
 [3,4]
 3*1+4*2=11
 [4,5]
 4*1+5*2=14.....MAX
 '''







nos=int(input())
sz=int(input())
arr=list(map(int,input().split()))
mx=-1
for i in range(0,len(arr)-sz+1):
    temp=arr[i:i+sz]
    k,s=1,0
    for j in temp:
        s+=(j*k)
        k+=1
    if s>mx:
        mx=s
print(mx)
    

'''
5
2
1 2 3 4 5
14
    
'''

