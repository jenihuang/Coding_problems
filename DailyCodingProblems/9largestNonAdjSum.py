'''
sum largest non adjacent nums in list
[2,4,6,2,5] returns 2,6,5 sum; [5,1,1,5] reterns 5,5 sum
constant time and space

find index of largest number

'''

def largest_non_adjacent(arr):
    if not arr:
    	return 0

    return max(
            largest_non_adjacent(arr[1:]),
            arr[0] + largest_non_adjacent(arr[2:]))

print(largest_non_adjacent([2,4,6,2,5]))

