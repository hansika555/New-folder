#print the shortest word
'''
s="Anusha yesu Ramana"
l=s.split()
print(l)
mini=1000
for word in l:
    if len(word)<mini:
        mini=len(word)
print(mini)
for word in l:
    if len(word)==mini:
        print(word)
'''
'''
s="Hansika reddy kalluri"
l=s.split()
print(l[::-1])
'''
'''
s1=list(input().split(","))
s2=list(input().split(","))
print(s1+s2)
'''
'''
def is_prime(n):
    if n==1:
        return False
    for f in range(2,n):
        if n%f==0:
            return False
    return True
def prime_galore(l):
    count=0
    k=[]
    for i in range(len(l)):

        if is_prime(i) and is_prime(l[i]):
            count+=1
            k.append(l[i])
    return k,count
print(prime_galore([1,3,11,18,17,23,6,8,10]))

'''
'''
a=int(input())
b=int(input())
print("*"*b)
for i in range(a-2):
    print('*'+" "*(b-2)+"*")
print("*"*b)
    '''
'''
def survival(T):
    for x in range(6):  # x from 0 to 5
        for y in range(6):  # y from 0 to 5
            temp = 30 + x**2 + y**2 - 3*x - 4*y
            if temp <= T:
                return True
    return False
print(survival(int(input())))
'''
n=int(input())
if n%2==0 and len(str(n))==10:
    print(True)
else:
    print("False")