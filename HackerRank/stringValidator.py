if __name__ == '__main__':
    s = input()
    sList = []
    for letter in s:
    	sList.append(letter)

    check1 = False
    check2 = False
    check3 = False
    check4 = False
    check5 = False

    for i in sList:
    	if i.isupper():
    		check5 = True
    	if i.islower():
    		check4 = True
    	if i.isdigit():
    		check3 = True

    if check4 or check5:
    	check2 = True
    if check3 or check2:
    	check1 = True


    print(check1)
    print(check2)
    print(check3)
    print(check4)
    print(check5)
