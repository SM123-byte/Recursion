print(f"\nFLIP IT WITH RECURSION\n")

print("\n PART 1: Extracting Digits")
number = 4827
print(f"Original Number: {number}")
while number > 0:
    number, last_digit = divmod(number, 10) #Found new function of divmod which does both the functions at the same time
    print(f"Last Digit: {last_digit} | Remaining Number: {number}")

def reverse_number(num, current=0):
    if num == 0: return current
    return reverse_number(num // 10, current * 10 + num % 10)

print("\n PART 2: Reversing a Number")
num = 4827
print(f"Original Number: {num}\nReversed Number: {reverse_number(num)}")

def reverse_string(text):
    return text if len(text) <= 1 else reverse_string(text[1:]) + text[0]

print("\nPART 3: Reversing a String")
word = "REVERSE"
print(f"Original String: {word}\nReversed String: {reverse_string(word)}")

def is_power_of_4(num):
    if num <= 1: return num == 1
    return num % 4 == 0 and is_power_of_4(num // 4)

print("\n PART 4: Checking Powers of 4")
test_nums = [1, 4, 8, 16, 20, 64, 100, 256]
for value in test_nums:
    print(f"{value:3d} is power of 4: {is_power_of_4(value)}")

summary_text = (
    f"\n\nFLIP IT WITH RECURSION SUMMARY\n\n"
    "Extracts the last digit and updates the main number cleanly.\n"
    "Tail Accumulators: Reverses integers\n"
    "Slicing Inverse: Reorders the strings.\n"
#Final summary
)
print(summary_text)
