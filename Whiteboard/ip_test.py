def checkIPs(ip_array):
    # Write your code here
    results = []

    for item in ip_array:
        if is_ip4(item):
            results.append('IPv4')
        elif is_ip6(item):
            results.append('IPv6')
        else:
            results.append('Neither')

    return results


def is_ip4(chars):
    '''checks if a string conforms to ip4 and returns True if yes, else False'''
    nums = chars.split('.')
    if len(nums) != 4:
        return False
    for num in nums:
        try:
            value = int(num)
            if value not in range(0, 256):
                return False
        except ValueError:
            return False
    return True


def is_ip6(chars):
    '''checks if a string conforms to ip6 and returns True if yes, else False'''
    items = chars.split(':')
    if len(items) not in range(3, 9):
        return False
    for item in items:
        if len(item) > 4:
            return False
        for char in item:
            if not char:
                continue
            ascii_value = ord(char)
            if ascii_value in range(48, 58) or ascii_value in range(65, 91) or ascii_value in range(97, 122):
                continue
            else:
                return False
    return True


# print(is_ip6('::'))
print(is_ip6('2001:db8::ff00:42:8329'))
# print(checkIPs(['This line has junk text.', '121.18.19.20']))
