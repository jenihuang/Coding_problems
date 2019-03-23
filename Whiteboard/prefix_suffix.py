def calculateScore(text, prefixString, suffixString):
    p_index = prefix_score(text, prefixString)
    s_index = suffix_score(text, suffixString)

    return text[p_index:s_index + 1]


def prefix_score(text, prefixString):

    max_score = {'score': 0, 'index': None}

    for i in range(len(text)):
        count = 0
        inner_count = 0
        for j in range(len(prefixString)):
            if prefixString[j] == text[i]:
                # match_index = 1
                inner_count = 1
                while j + inner_count < len(prefixString) and i + inner_count < len(text) and prefixString[j + inner_count] == text[i + inner_count]:
                    inner_count += 1
            if inner_count > max_score['score']:
                max_score['score'] = inner_count
                max_score['index'] = i

    return max_score['index']


def suffix_score(text, suffixString):

    max_score = {'score': 0, 'index': None}

    for i in range(len(text) - 1, -1, -1):
        count = 0
        inner_count = 0
        for j in range(len(suffixString)):
            if suffixString[j] == text[i]:
                # match_index = 1
                inner_count = 1
                while j + inner_count < len(suffixString) and i + inner_count < len(text) and suffixString[j + inner_count] == text[i + inner_count]:
                    inner_count += 1
            if inner_count > max_score['score']:
                max_score['score'] = inner_count
                max_score['index'] = i

    return max_score['index'] + max_score['score'] - 1

# print(all_substrings('nothing'))
print(calculateScore('ab', 'b', 'a'))
print(calculateScore('nothing', 'bruno', 'ingenious'))
# print(prefix_score('ab', 'b'))
# print(prefix_score('nothing', 'bruno'))
# print(suffix_score('ab', 'a'))
# print(suffix_score('nothing', 'ingenious'))
