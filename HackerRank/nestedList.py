#iterate through list data
#make a dictionary key is score value is name
#make a set with grades
#remove min from set
#find new min from set in dictionary
#return values

d ={}
grades = set()

if __name__ == '__main__':
	for _ in range(int(input())):
		name = input()
		score = float(input())


		d.setdefault(score, [])
		d[score].append(name)
		grades.add(score)

grades.remove(min(grades)) #removes the lowest grade

lookup = min(grades) #value to return is the second lowest grade in original list
final = sorted(d[lookup])

for i in final:
	print(i)
