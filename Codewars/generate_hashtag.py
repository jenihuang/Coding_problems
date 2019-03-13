def generate_hashtag(s):

    if len(s) == 0:
        return False

    str_list = s.split(' ')
    results = ['#']

    for word in str_list:
        results.append(word.title())

    results_str = ''.join(results)

    if len(results_str) > 140:
        return False
    else:
        return results_str


print(generate_hashtag('Hello there thanks for trying my Kata'))
