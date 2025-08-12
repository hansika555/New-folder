def Linear_search(p_list,p_target):
    for i,value in enumerate(p_list):
        if value == p_target:
            return i
    return -1
print(Linear_search([1,2,3,4,5,6],5))
l1=[1,2,6,7,3,2]
l1.sort()
print(l1)
s1="hansika"
s1=s1.capitalize()
print(s1)

prev_list=[-1,2,-3,4]
new_list=[i**2 for i in prev_list if i<0]
print(new_list)

s="my name is Elshad"
new_list=[a for a in s if (a.lower() not in "aeiou ")]
print(new_list)
print("".join(new_list))
a=[1,2,3,4,5]
print(a[3:0:-1])
