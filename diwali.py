#DIWALI CONTEST
'''
INPUT
6
180
OUTPUT
4'''
p=int(input())
t=int(input())
c=0
r=4*60-t
x=0
for i in range(1,p+1):
    x+=i*5
    if x>r:
        break
    c=c+1
print(c)

6
180
4






   
     
p=int(input())
t=int(input())
c=0
r=4*60-t
x=0
for i in range(1,p+1):
    if x<r:
        x+=i*5
        c=c+1
print(c)




6
180
4
