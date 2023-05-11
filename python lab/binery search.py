'''
binery search in python
'''

arr = [ 2, 3, 4, 10, 40 ]
x = 40

low = 0
high = len(arr)
'''mid = (low+high)//2'''
while(low<=high):
    mid = (low+high)//2
    if(arr[mid]==x): 
        print(mid)
        break
    elif(arr[mid]>x): high = mid-1
    else: low= mid+1
