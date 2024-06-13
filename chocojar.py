#CHOCOLATE JAR
'''INPUT
10 20 30
3
OUTPUT
21'''

a=list(map(int,input().split()))
n=int(input())
count=0
for i in a:
    count=count+(i//3)
    x=i%3
    if x!=0:
        count=count+1
print(count)
    
'''10 20 30
3
21




30 40 
2
24

'''
        
