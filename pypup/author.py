# def product_digits(a):
#     return (a % 10) * (a // 10)

# print(product_digits(77)


# def sum_digits(a):
#     last_digit = a % 10
#     a = a // 10
#     middle_digit = a % 10
#     first_digit = a // 10
#     sum = last_digit + middle_digit + first_digit
#     return sum

# def sum_digits(a):
#     last_digit = a % 10
#     a = a // 10
#     middle_digit = a % 10
#     first_digit = a // 10
#     sum = last_digit + middle_digit + first_digit
#     return (a % 10) + (a // 10) + (a // 10 % 10)

# def sum_digits(a):
#     return (a % 10) + (a // 10 % 10) + (a // 10 // 10)

def convert_seconds(s):
    return [s // 60, s % 60]

print(convert_seconds(200))