def cakes(recipe, available):

    new = []

    for item, qty in recipe.items():
        if item in available:
            new.append(available[item] // qty)
        else:
            return 0

    return min(new)


print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {
      'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
