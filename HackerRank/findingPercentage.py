#start a new dictionary object
#using .split() make index 0 (name) the key and the remaining items values


from decimal import *

if __name__ == '__main__':
	TWOPLACES = Decimal(10)** -2
	n = int(input())
	student_marks = {}
	for _ in range(n):
		name, *line = input().split()
		scores = list(map(float, line))
		student_marks[name] = scores
	query_name = input()

	final = student_marks[query_name]
	final = list(final)
	average = sum(final)/3
	print(Decimal(average).quantize(TWOPLACES))
