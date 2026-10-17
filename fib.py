def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

input("Tree recursion - two recusive calls per steps. Press Enter: ")
print(" fib(5) = ", fib(5))
print(" fib(6) = ", fib(6))

n = int(input("Enter n (try 4 or 6): "))
guess = input("What is fib(" + str(n) + ")?")
input("Fibonacci: fib(n) = fib(n - 1) + fin(n - 2) base: fib(0) = 0 fib(1) = 1. Press Enter: ")
print(" fib(" + str(n) + ") = ", fib(n), " your guess:", guess)
