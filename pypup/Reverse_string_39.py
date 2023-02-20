def reverse_string(a):
    new_str = ""
    length = len(a) - 1
    while length >= 0:
        new_str += a[length]
        length = length - 1
    return new_str

print(reverse_string('abc'))