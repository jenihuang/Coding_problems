'''
columns j 0 - 3 are starting points
rows i 0 - 3 are starting points
total = 0
for loop through these indices
count = top + mid + bottom
if count > total, set total = count
reset count to zero
'''
def hourglassSum(arr):
    total = None
    for i in range(0,4):
        for j in range(0,4):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bottom = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            count = top + mid + bottom
            if total == None or count > total:
                total = count
            count = 0

    return total



