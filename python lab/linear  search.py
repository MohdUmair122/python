''' linear search '''
arr = [2, 3, 4, 10, 40]
x = int(input("enter the number that you want to find : "))
N = len(arr)
for i in range(0, N):
    if (arr[i] == x):
        print(i)
