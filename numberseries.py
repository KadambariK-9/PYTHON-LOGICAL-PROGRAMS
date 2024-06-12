
'''6 28 66 120 190 276....378
  ---difference------
22 38 54 70 86
+  +  +  +  +
16 16 16 16

2*3
4*7
6*11
8*15
10*19
12*23
14*27



n=6
k=22
for i in range(1,7):
    print(n)
    n=n+k
    k=k+16



a=2
b=3
for i in range(1,7):
    n=a*b
    print(n)
    a=a+2
    b=b+4

'''

12,14,2,16,5,3


a=list(map(int,input().split()))
for i in a:
    if i<a[i]:
        print(i)
    else:
        print(a[i])







