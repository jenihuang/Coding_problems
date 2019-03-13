#make a base case is 1 which returns 1
#all other cases return self plus simpleAdding(num-1)

def SimpleAdding(num):
    if num == 1:
        return 1
    else:
        return num + simpleAdding(num-1)

print(SimpleAdding(140))
