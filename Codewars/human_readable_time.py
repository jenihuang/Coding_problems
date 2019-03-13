def make_readable(seconds):

    if seconds:
        h = seconds // 3600
        if h < 10:
            str_h = '0' + str(h)
        else:
            str_h = str(h)
        m = (seconds - h * 3600) // 60
        if m < 10:
            str_m = '0' + str(m)
        else:
            str_m = str(m)
        s = seconds - h * 3600 - m * 60
        if s < 10:
            str_s = '0' + str(s)
        else:
            str_s = str(s)
        return('{}:{}:{}'.format(str_h, str_m, str_s))
    else:
        return('00:00:00')
