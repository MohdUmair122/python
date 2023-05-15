row1 = int(input("Enter the no. of row1 : "))
col1 = int(input("Enter the no. of col1 : "))


row2 = int(input("Enter the no. of row2 : "))
col2 = int(input("Enter the no. of col2 : "))

if(row2!=col1):
    print("Multiplication is not valid")
else:
    mat1 = [[0 for _ in range(col1)] for _ in range(row1)]
    mat2 = [[0 for _ in range(col2)] for _ in range(row2)]
    result = [[0 for _ in range(col2)] for _ in range(row1)]

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
     
    #Multiplication of two matrix
    # iterating by row of mat1
    for i in range(len(mat1)):
 
        # iterating by column by mat2
        for j in range(len(mat2[0])):
 
            # iterating by rows of mat2
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
            
    # printing a result matrix
    for r in result:
        print(r)      
