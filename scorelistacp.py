# All combined codes
print(f"\nSCORE LIST EXPLORER\n")

scores = [45, 60, 75, 88, 92]
print(f"Score List: {scores}")

print("\nPART 1: Head-Tail Pattern ")
print(f"Full List: {scores}\nHead: {scores[0]}\nTail: {scores[1:]}")

def show_shrink(lst):
    print(f"Current list: {lst}")
    if len(lst) == 1:
        return print(f"Base case reached: {lst}") # Base case
    show_shrink(lst[1:])

print("\n PART 2: Base Case for Lists")
show_shrink(scores)

def is_sorted(lst):
    if len(lst) <= 1: return True
    return lst[0] <= lst[1] and is_sorted(lst[1:])

print("\n PART 3: Sorted Check with Recursion")
for s in [scores, [45, 88, 60, 75, 92]]:
    print(f"List: {s} | Is sorted? {is_sorted(s)}")

def recursive_sum(lst):
    return 0 if not lst else lst[0] + recursive_sum(lst[1:])

print("\n PART 4: Sum of a List with Recursion")
print(f"Total Score: {recursive_sum(scores)}")

def largest_score(lst):
    if len(lst) == 1: return lst[0]
    return max(lst[0], largest_score(lst[1:]))

print("\nPART 5: Largest Element with Recursion")
print(f"Highest Score: {largest_score(scores)}")

summary_text = (
    f"\n\nSCORE LIST EXPLORER SUMMARY\n\n"
    "Head: The first item in a list (lst[0]).\n"
    "Tail: All remaining items in a list (lst[1:]).\n"
    "Base Case: Halts recursion (often when list length is 0 or 1).\n"
    "Operations: Slicing breaks data down smoothly without track indices.\n"
# Final summary
)
print(summary_text)
