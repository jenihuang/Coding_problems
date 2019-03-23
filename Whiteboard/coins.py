def coins(arr,amount):
    '''given coins, print all ways to make amount'''

    output = [0]*(amount+1)
    output[0] = 1

    for a in arr:
        index = a
        while index < len(output):
            output[index] = output[index-a] + output[index]
            index += 1

    return output[-1]


print(coins([1,2,5], 7))



