from array import *
#1.create and traverse through arrays
arr1=array('i',[1,2,3,4,5])
for i in arr1:
    print(i)
#2.Access individual elements through indexes
print("Step 2")
print(arr1[0])
#3.Append any value
print("Step 3")
arr1.append(6)
print(arr1)
#4.insert
print("Step 4")
arr1.insert(0,0) #time consuming
print(arr1)
#5.extend
print("Step 5")
arr1.extend([7,8])
print(arr1)
#6.use fromlist()
print("Step 6")
l=[20,21,22]
arr1.fromlist(l)
print(arr1)
#7.remove
print("Step 7")
arr1.remove(22) #fastest
print(arr1)
#8.pop
print("Step 8")
arr1.pop() #removes last ele
print(arr1)
#9.find index
print("Step 9")
print(arr1.index(20))
#10.reverse
print("Step 10")
arr1.reverse()
print(arr1)
#11.buffer info
print("Step 11")
print(arr1.buffer_info())
#12.count
print("Step 12")
print(arr1.count(22))
#13.conv array to string
print("Step 13")
strTemp = arr1.tobytes()
print(strTemp)
#14.conv array to list
print("Step 14")
strList = arr1.tolist()
print(strList)
#15.slice elements
print("Step 15")
print(arr1[1:4])