'''printing permutations of a string'''


def print_permute(lst):

    print_permute_helper([], lst)


def print_permute_helper(current, remainder):

    if not remainder:
        print(current)
    else:
        for i in range(len(remainder)):
            new_current = current + [remainder[i]]
            new_remainder = remainder[:i] + remainder[i + 1:]
            print_permute_helper(new_current, new_remainder)


print_permute([1, 2, 3])
