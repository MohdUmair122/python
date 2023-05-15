row = int(input("Enter the no. of row : "))
col = int(input("Enter the no. of row : "))

#Initializing a matrix
mat = [[0 for _ in range(col)] for _ in range(row)]

#Taking input from User
for i in range(0,row):
    for j in range(0,col):
        mat[i][j] = 0
        a = int(input())
        mat[i][j] = a

# printing a matrix
for i in range(0,row):
    for j in range(0,col):
        print(mat[i][j], end=" ")
    print()
