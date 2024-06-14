#REVERSE NUMBER AND SQUARE OF IT WITHOUT USING STRING
def rev(n):
    revno=0
    while n>0:
        dig=n%10
        revno=revno*10+dig
        n=n//10
    return revno**2
inp=167
ans=rev(inp)
print(ans)
        
