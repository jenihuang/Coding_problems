def fizzBuzz(max_num):
    """prints fizz for nums divisible by 3, buzz for 5, fizzbuzz for 15"""
    # reversed range down and check for 15, elif 3, elif 5, else just number

    for i in reversed(range(1, max_num + 1)):

        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


fizzBuzz(100)
