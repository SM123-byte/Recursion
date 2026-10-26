def flip_number(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flip_number(num // 10)
    return last * pow(10, len(str(rest))) + rest

input("flip Number peels the last digit with % 10 then recurses on // 10. Press Enter: ")
print(" flip_number(123) = ", flip_number(123))
print(" flip_number(456) = ", flip_number(456))

n = int(input("Enter a number (try 789 or 1234): "))
guess = input("What is flip number(" + str(n) + ")?")
input("flip_number peels the last digit and places it at the front each step. Press Enter: ")
print(" flip_number(" + str(n) + ") =", flip_number(n), " your guess:", guess)