# Both Matrices have to be in a same Order

row1 = int(input("Enter the no. of row1 : "))
col1 = int(input("Enter the no. of col1 : "))


row2 = int(input("Enter the no. of row2 : "))
col2 = int(input("Enter the no. of col2 : "))

#Initializing a matrix
mat1 = [[0 for _ in range(col1)] for _ in range(row1)]
mat2 = [[0 for _ in range(col2)] for _ in range(row2)]

resultSum = [[0 for _ in range(col1)] for _ in range(row1)]

resultDiff = [[0 for _ in range(col1)] for _ in range(row1)]

#Taking input from User
for i in range(0,row1):
    for j in range(0,col1):
        mat1[i][j] = 0
        a = int(input())
        mat1[i][j] = a

for i in range(0,row2):
    for j in range(0,col2):
        mat2[i][j] = 0
        a = int(input())
        mat2[i][j] = a

#sum of two matrix
for i in range(0,row2):
    for j in range(0,col2):
        resultSum[i][j] = mat1[i][j] + mat2[i][j] 
        
# printing a result matrix
for i in range(0,row1):
    for j in range(0,col1):
        print(resultSum[i][j], end=" ")
    print()
    
#Difference of two matrix
for i in range(0,row2):
    for j in range(0,col2):
        resultDiff[i][j] = mat1[i][j] - mat2[i][j] 

 # printing a result matrix
for i in range(0,row1):
    for j in range(0,col1):
        print(resultDiff[i][j], end=" ")
    print()       
