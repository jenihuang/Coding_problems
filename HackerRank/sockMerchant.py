# n represents number of socks total, ar lists the socks represented by numbers
# make ar into a set
# for each item in the set count how many are in the list 
# total = integer divide number by 2
# pairs is the total pairs, pairs += total for each unique number
def sockMerchant(n, ar):
    pairs = 0
    unique = set(ar)
    for i in unique:
        total = ar.count(i)//2
        pairs += total
    return pairs


print(sockMerchant(6,[2,2,2,1,1,1,3,3,3]))

