from collections import Counter


def anagrams(word, words):

    c = Counter(word)

    results = []

    for word in words:
        if Counter(word) == c:
            results.append(word)

    return results


print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
