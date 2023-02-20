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

# def convert_seconds(s):
#     return [s // 60, s % 60]

# print(convert_seconds(200))

# # solution: 1
# def greatest_number(a ,b):
#     if a < b:
#         greatest_number = b
#     else: 
#         greatest_number = a
#     return greatest_number

# print(greatest_number(14, 2))

# # Solution: 2
# def greatest_number(a, b):
#     if a < b:
#         return b
#     else:
#         return a

# Solution: 3
# def greatest_number(a, b):
#     greates_number = max(a, b)
#     return greates_number

# Solution: 4
# def greatest_number(a, b):
#     greatest_number = a if a > b else b
#     return greatest_number

# def greatest_number_three(a,b,c):
#     if a < b:
#         if c < b:
#             return b
#         else: 
#             return c
#     elif c < a:
#         return a
#     else:
#         return c 
    

# def even_num(a,b,c):
#     sum = 0
#     if a % 2 == 0:
#         sum = sum + a
#     if b % 2 == 0:
#         sum = sum + b
#     if c % 2 == 0:
#         sum = sum + c
        
#     return sum

# print(even_num(2,3,12))


# def seconds_converter(a):
#     hours = 0
#     minutes = 0
#     if(a // 3600 > 0):
#         hours = a // 3600
#         a = a - hours * 3600
#     if(a // 60 > 0):
#         minutes = a // 60
#         a = a - minutes * 60

#     seconds = a
    
#     return [hours, minutes, seconds]

# print(seconds_converter(1721))

# def hours_converter(hours):
#     return [hours // 24, hours - (hours // 24) * 24]

# print(hours_converter(70))

# def convert_to_hours(days, hours):
#     total_hours = days * 24 + hours
#     return total_hours

# print(convert_to_hours(2, 5))
# def convert_months(months):
#     return months // 12, months - (months // 12 * 12)

# print(convert_months(22))

# def lowest_number(a,b,c,d):
#     if a > b:
#         if a > c:
#            if a > d:
#                return a
#            else:
#                return d
#         elif c > d:
#             return c
#         else:
#             return d
#     elif b > c:
#         if b > d:
#             return b
#         else:
#             return d
#     elif c > d:
#         return c
#     else:
#         return d
    
# print(lowest_number(112,222,13,412))   

# def n_times(s, n):
#     total =  s if n == 1 else 0
#     for i in range(1,n):
#         total += s        

#     return total

# print(n_times(3, 1))

# def n_power_2(n):
#     return 2 ** n
# print(n_power_2(4))

# def n_power_a(a, n):
#     return a ** n

# print(n_power_a(2, 5))

# def criteria_level(gpa):
#     if(gpa == 4):
#         return "Excellent"
#     elif(gpa >= 3):
#         return 'Good'
#     elif(gpa >= 2):
#         return 'Nod bad'
#     else:
#         return "Worst"
    
# print(criteria_level(4))

def week_number_text(day):
    if day == 1:
        return 'Monday'
    elif day == 2:
        return 'Tuesday'
    elif day == 3:
        return 'Thursday'
    elif day == 4:
        return 'Wednesday'
    elif day == 5:
        return 'Friday'
    elif day == 6:
        return 'Saturday'
    else:
        return 'Sunday'

print(week_number_text(4))