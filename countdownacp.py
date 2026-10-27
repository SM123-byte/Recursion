# More or less same function as exemplar code

print(f"\nMY COUNTDOWN TIMER CHALLENGE\n")

def countdown(number):
    if number == 0:
        return print("Time is up!")
    print(number)
    countdown(number - 1)

print("\nPART 2: Countdown from 5")
countdown(5)

def build_and_unwind(level):
    if level == 0:
        return print("Base case reached. Now unwinding begins.")
    print(f"Building level: {level}")
    build_and_unwind(level - 1)
    print(f"Unwinding level: {level}")

print("\nPART 3: Build and Unwind Demo")
build_and_unwind(3)

def count_up(number):
    if number <= 10:
        print(number)
        count_up(number + 1)

print("\nPART 4: Counting from 1 to 10")
count_up(1)

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print("\nPART 5: Factorial Result")
print(f"5! = {factorial(5)}")

def unsafe_countdown(number):
    try:
        unsafe_countdown(number - 1) # Added New Exception Handlind block
    except RecursionError:
        print(f"Caught standard Stack Overflow at level {number}!")

print("\nPART 6: Stack Overflow Safety Demo")
unsafe_countdown(1)

summary_text = (
    f"\n\nRECURSION CHALLENGE SUMMARY\n\n"
    "Recursion: A function that calls itself.\n"
    "Base Case: The condition that stops recursion.\n"
    "Build & Unwind: Stack frames open up, hit the base case, then resolve backwards.\n"
    "Factorial: Standard multiplication recursion pattern.\n"
    "Stack Overflow: Occurs if the base case is missing or recursion limit is hit.\n"
)
#Quick summary
print(summary_text)
