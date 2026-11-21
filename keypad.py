def tower_of_hanoi(disks, source, helper, destination):  # Arguments that help move the disks easier
    if disks == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(disks - 1, source, destination, helper)
    print(f"Move disk {disks} from {source} to {destination}")
    tower_of_hanoi(disks - 1, helper, source, destination)

tower_of_hanoi(3, "A", "B", "C")

keypad = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
} # Dictionary for keypad

def generate_words(digits, current_word=""):
    if not digits:
        print(current_word)
        return
    for letter in keypad[digits[0]]:
        generate_words(digits[1:], current_word + letter)

number = "23"
print("Digits:", number)
print("Possible words:")
generate_words(number)

def show_recursion_tree(digits, current_word="", level=0):
    indent = "  " * level
    if not digits:
        print(f"{indent}Word completed: {current_word}")
        return
    print(f"{indent}Current word: {current_word} | Next digit: {digits[0]}")
    for letter in keypad[digits[0]]:
        show_recursion_tree(digits[1:], current_word + letter, level + 1)

show_recursion_tree("23")