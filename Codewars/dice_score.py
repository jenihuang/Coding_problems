from collections import Counter


def score(dice):

    scores = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
    single = {1: 100, 5: 50}

    c = Counter(dice)

    points = []

    for num, count in c.items():
        if count == 3:
            points.append(scores[num])
        elif count == 2 and num in single:
            points.append(single[num] * 2)
        elif count == 1 and num in single:
            points.append(single[num])
        elif count == 4:
            points.append(scores[num])
            if num in single:
                points.append(single[num])
        elif count == 5:
            points.append(scores[num])
            if num in single:
                points.append(single[num] * 2)
        else:
            continue

    if points:
        total = sum(points)
    else:
        total = 0
    return total
