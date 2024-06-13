#ENCODE THE NUMBER
'''
INPUT
167
OUTPUT
13649
'''




n=int(input())
a=str(n)
x=0
ad=''
for i in a:
    sq=i**2
    sr=str(sq)
    ad+=sr
print(ad)



















'''

INPUT:167
OUTPUT: 49361



n=167
def sod(n):
    c=0
    while n>0:
        c=c+1
        n=n//10
    return c
print(sod(n))
def rev(n):
    ans=0
    while n>0:
        dig=n%10
        sq=dig**2
        sod_sq=sod(sq)
        ans=ans*(10**sod_sq)+sq
        n=n//10
    return ans
print(rev(n))
ans=rev(n)
def rev2(n):
    ans2=0
    while n>0:
        dig=n%10
        ans2=ans2*10+dig
        n=n//10
    return ans2
print(rev2(ans))




3
49361
16394
'''









'''
inp=int(input())
strr=str(inp)
d=0
for i in strr:
    s=int(i)
    x=s**2
    st=str(x)
    p=map(str,st+st)
print(p)
'''
