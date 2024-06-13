#ANT AND RAIL
n=int(input())
arr=list(map(int,input().split()))
s=0
ans=0
i=1
for i in arr:
    s=s+i
    if s==0:
        ans=ans+1
print(ans)


5
1 -1 1 -1 1
2
