
#prints array backwards as a string with spaces

arr = [1,2,3,4]
newAr = []
for i in reversed(range(0,len(arr))):
    newAr.append(str(arr[i]))
print(" ".join(newAr))







