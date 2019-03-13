def count_smileys(arr):
    valid = [":)", ";)", ":D", ";D", ":-)", ":~)",
             ";-)", ";~)", ":-D", ":~D", ";-D", ";~D"]
    count = 0
    for i in arr:
        if i in valid:
            count += 1
    return count
