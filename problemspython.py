'''x=int(input())
if x%2==0:
    print("even number")
else:
    print("odd number")
print(".fine...")
'''
'''x=int(input())
y=int(input())
if 18<=x<=55 and y>45:
    print(1)
else:
    print(0)
print("bye")    
   ''' 
'''x=int(input())
y=int(input())
if 18<=x<=55 or y>45:
    print(1)
else:
    print(0)'''
'''amt=int(input())
if amt>250:
    amt=amt-40
    print(amt)
else:
    print(amt)
'''
'''
day=input()
if day=="sunday" or day=="Sunday" or day=="SUNDAY":
    print("holiday")
else:
    print("shut and go to scholl")'''
'''s=int(input())
if s<=120:
    print("cass")
else:
    print("seminar hall")
'''
'''x=int(input())
if x>=10:
 print("riding bus")
else:
    print("riding car")
'''
'''x=int(in
      put())
if x==0:
    print(0)
elif x>0:
    print("positie")
else:
    print("negative")
'''
'''
cp=float(input("cost prie"))
sp=float(input("selling price"))
if sp>cp:
    print("profit:$%.2f"%(sp-cp))
elif sp<cp:
    print("loss:$%.2f"%(cp-sp))
else:
    print("no differ:$%.2f"%(cp-sp))'''


'''s=int(input("salary details"))
if 40000>s>25000:
    print("manager")
elif 25000>=s>15000:
    print("accountant")
elif s<=15000:
    print("clerk")'''







'''days=int(input())
if 1<=days<=5:
    print("$%d"%15)
elif 6<=days<=10:
    print("$%d"%50)
elif 30>=days>10:
    print("$%d"%100)
elif days>30:
    print(" membership canceled")
else:
    print("it's ok.")
'''
'''ch=input()
if ch==("N" or  "n"):
    print("north")
elif ch==("S" or "s"):
    print("south")
elif ch==("w" or "W"):
    print("west")
elif ch==("e" or "E"):
    print("east")
'''
'''num=int(input())
if num>=0:
    if num==0:
        print("zero")
    else:
        print("+ve num")
else:
    print("-ve num")

for i in range(5):
    print(i,end='')

for i in range(10,16):
    print(i,end='')

for i in range(20,30,2):
    print(i,end='')

for i in range(22,11,-4):
    print(i,end=' ')
 
for i in range(22,11,-4):
 print(i)

x=int(input())
y=int(input())
if x<y:
    for i in range(x,y+1):
        print(i,end=' ')
else:
    for i in range(y,x+1):
        print(i,end=' ')

x=int(input())
y=int(input())
if(range(x,y)):
    for i in range(x,y+1):
        print(i,end=' ')
else:
    for i in range(y,x+1):
        print(i,end=' ')

x=int(input())
y=int(input())
if x>y:
    for i in range(y,x+1):
        print(i,end=' ')
else:
    for i in range(x,y+1):
        print(i,end=' ')
'''
'''x=int(input())
y=int(input())
if x>y:
    s=y
    l=x
else:
    s=x
    l=y
for i in range(s,l+1):
    print(i,end=' ')

'''
'''n=int(input())
s=0
for i in range(n):
    x=float(input("enter the number %.f:"%(i+1)))
    s=s+x
    print(int(s))
print(int(s/n))
'''
'''for i in range(1,50):
    if i%2!=0:
        print(i,end=' ')
'''
'''n=int(input())
for i in range(1,11):
  print("%2d*%2d=%2d"%(n,i,n*i))
'''
'''n=int(input())
s=0
for i in range(n):
    n1=float(input())
    s=s+int(n1)
    a=s/int(n1)
print(f"the average of {n} numbers is :{a:.2f}")
'''
'''n=int(input())
for i in range(1,n+1):
    n1=n//10
    n2=n%10
print(n1+n2)
'''
'''n=int(input())
s=0
for i in str(n):
    s=s+int(i)
    print(i)
print(s)
'''
'''n=int(input())
s=0
n_str=str(n)
for i in n_str:
    d=int(i)
    s=s+d
print(f"the sum of digits of {n} is :{s}")
'''
'''
n=int(input())
cnt=0
for i in range(2,n):
    if n%i==0:
        cnt=cnt+1
if cnt==0:
    print("prime")
else:
    print("not prime")
'''
'''
n=int(input())
cnt=0
for i in range(1,n+1):
    if n%i==0:
        cnt=cnt+1
if cnt==2:
    print("prime")
else:
    print("not prime")
'''
'''n=int(input())
if n<=1:
    is_prime=False
else:
    is_prime=True
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
if is_prime:
    print(f"{n} is a prime number")
else:    
    print(f"{n} is not a prime number")
'''
'''n=int(input())
t=n
rev=0
num_str=str(n)
num_dgt=len(num_str)
//print(num_dgt)
for i in range(num_dgt):
    dgt=n%10
    rev=rev*10+dgt
    n=n//10
//print(n)
print(f"the reverse of {t} is:{rev}")
'''
'''n=int(input())
t=n
rev=0
num_str=str(n)
num_dgt=len(num_str)
for i in range(num_dgt):
    dgt=n%10
    rev=rev*10+dgt
    n=n//10
if t==rev:
    print(t,"is palindrome")
else:    
    print(t,"is palindrome")
'''
'''n=int(input("enter the value of n"))
f,s=0,1
print("fibonacci series")
for i in range(n):
    print(f,end=" ")
    f,s=s,f+s
print(f,s)'''



'''for i in range(1,6):    1 1 1
    for j in range(1,6):   2 2 2
        print(i,end=" ")   3 3 3
    print()    
'''
'''for i in range(1,6):     1 2 3
    for j in range(1,6):    1 2 3
        print(j,end=" ")    1 2 3
    print()    
'''
'''for i in range(1,4):    
    for j in range(1,6):
        print(i,end=" ") 
    print()    
'''
'''for i in range(1,6):    
    for j in range(1,4):
        print(i,end=" ")
    print()    
'''
'''for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
        
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,6-i+1):
        print(j,end=" ")
    print()
      
'''
'''
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
'''for i in range(1,6):
    for j in range(5,i-1,-1):
        print(i,end=" ")
    print()
'''
'''for i in range(5,0,-1):
    print(i)
'''
'''for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(j,end=" ")
    print()
'''
'''
for i in range(1,6):
    for j in range(1,6):
        print("%2d"%(i*j),"\t",end=" ")
    print()
'''
'''for i in range(6,0,-1):
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
'''


'''n=int(input())
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
print(rev)
'''
'''n=int(input())
while(n==str(n)):

    print(n)
'''
'''for num in range(5):
    print(f"current number:{num}")
else:
    print("loop completed normally")
'''
'''for num in range(5):
    print(f"current number:{num}")
    if num==3:
           break
else:
    print("loop completed normally")
'''
'''c=0
while c<10:
    print(f"current number:{c}")
    c=c+1
else:
    print("loop completed normally")
'''
c=0
while c<10:
    print(f"current number:{c}")
    c=c+1
    if c>5:
        break
else:
    print("loop completed normally")














































