def title_case(sentence):
    """uppcase first and last word, title case every word except a, an, the, and, in"""
    # split string to list and lower everything
    # make set for special case words a, an, and, in, of, the
    # loop through list and title every word except index 1 and index len(sentence)-1

    lower_words = ['a', 'an', 'and', 'in', 'of', 'the']

    split_sentence = sentence.split()
    lower_list = [word.lower() for word in split_sentence]

    for i in range(len(lower_list)):
        if lower_list[i] not in lower_words:
            lower_list[i] = lower_list[i].title()

        lower_list[0] = lower_list[0].upper()
        lower_list[-1] = lower_list[-1].upper()

    print(lower_list)


title_case('Hello this is a cat in a hat on the beach')
