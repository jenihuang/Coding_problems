from collections import Counter


def cakes(recipe, available):

    r = Counter(recipe)
    a = Counter(available)

    cakes = 0

    while a:
        a = (a - r)
        if len(a) > len(r) or a.keys() == r.keys():
            cakes += 1
        else:
            break

    return cakes


print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {
      'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
