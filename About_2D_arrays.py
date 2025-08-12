import numpy as np
TwoD=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
print(TwoD)
ele=int(input())
for i in range(len(TwoD)):
    for j in range(len(TwoD[0])):
        if TwoD[i][j]==ele:
            print(f"at row:{i+1} and a column {j+1}")       
