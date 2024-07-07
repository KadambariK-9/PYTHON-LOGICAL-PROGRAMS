'''
INPUT
aeiou
OUTPUT
NO OF VOWELS=5
NO OF CONSONANTS



a=input()
nv=0
nc=0
v='aeiou'
for i in a:
    if i in v:
        nv+=1
    else:
        nc+=1
print(f'no of vowels:{nv}')
print(f'no of consonants:{nc}')



aeiou
no of vowels: 5
no of consonants: 0

aeiouy
no of vowels: 5
no of consonants: 1




'''
s=input()
vowels,consonants=0,0
for i in range(len(s)):
    if s[i] in 'aeiou':
        vowels+=1
    else:
        consonants+=1
print(f'no of vowels:{vowels}')
print(f'no of consonants:{consonants}')
