import math
t=int(input())
assert 1<=t<=100

def func(n):
    digit=math.pow(2,n)
    rem=s=0
    while digit!=0:
        rem=digit%10
        s=rem+s
        digit=digit//10
    return int(s)

arr=[]
for i in range(t):
    n=int(input())
    assert 1<=n<=10**4
    arr.append(func(n))

for i in range(t):
    print(arr[i])

    
    """rem=s=0
    while digit!=0:
        rem=digit%10
        s=rem+s
        digit=digit//10
    arr=list(digit.strip())
    """

