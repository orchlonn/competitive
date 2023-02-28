# def fib(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1

#     if n in memo:
#         return memo[n]
    
#     memo[n] = fib(n - 1) + fib(n - 2)
#     return memo[n]

# memo = {}

def fib(n):
    # Base case of 2
    if n == 2:
        return 1
    # Base case of 1
    if n == 1:
        return 0
    # Our equation
    return fib(n - 1) + fib(n - 2)

print(fib(8))
