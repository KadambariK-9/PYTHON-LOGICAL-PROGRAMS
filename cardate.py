'''
INPUT
6
8
9871 4687 9687 2096 8769 8476 2968 7174

OUTPUT
1000



d=int(input())
n=int(input())
if n==0:
        print(-1)
cno=list(map(int,input().split()))
f=0
for i in cno:
    if d%2==0:
        if i%2!=0:
            f+=250
    else:
        if i%2==0:
            f+=250
print(f)



17.....DATE
6......NO OF CARS
1012 6683 8471 3685 5452 8403.......CAR NO
500....OUTPUT



6
8
9871 4687 9687 2096 8769 8476 2968 7174
1000
'''


date=int(input())
n=int(input())
if n==0:
    print(-1)
else:
    cars=list(map(int,input().split()))
    fine=0
    if date%2==0:
        for car in cars:
            if car%2!=0:
                fine+=250
    else:
        for car in cars:
            if car%2==0:
                fine+=250
    print(fine)











