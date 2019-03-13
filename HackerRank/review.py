'''
make variables odd and even
for loop range from 0 to n, every two and increment even var
for loop range from 1 to n, every two and increment odd var
return odd + "space" + even

'''
def printOddEven(s):
    odd = ''
    even = ''
    for i in range(0,len(s),2):
        odd += s[i]
    for i in range(1,len(s),2):
        even += s[i]
    print(odd + " " + even)

s = input()
s = s.split()
for i in s:
    try:
        t = int(i)
    except:
        printOddEven(i)
        
'''
the below solution works in editor
'''


for N in range(int(input())):
    S = input()
    print(S[::2], S[1::2])





