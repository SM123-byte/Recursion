# DIfferent types of recursion showed

print(f"\nSTACK FRAME VISUALIZER\n")

def linear_recursion(n):
    if n == 0: return
    print(f"Linear call at level: {n}")
    linear_recursion(n - 1)

print("PART 1: Linear Recursion")
linear_recursion(5)

def tail_recursion(n):
    if n == 0: return
    print(f"Tail work before call: {n}")
    tail_recursion(n - 1)

print("\nPART 2: Tail Recursion")
tail_recursion(5)

def head_recursion(n):
    if n == 0: return
    head_recursion(n - 1)
    print(f"Head work after call:  {n}")

print("\nPART 3: Head Recursion")
head_recursion(5)

def increasing_decreasing(n):
    if n == 0: return
    print(f"Going down:  {n}")
    increasing_decreasing(n - 1)
    print(f"Coming back: {n}")

print("\nPART 4: Increasing-Decreasing Recursion")
increasing_decreasing(5)

def tree_recursion(n, depth=0):
    if n == 0: return
    print(f"{'  ' * depth}Tree node: {n}")
    tree_recursion(n - 1, depth + 1)
    tree_recursion(n - 1, depth + 1)

print("\nPART 5: Tree Recursion")
tree_recursion(3)

summary_text = (
    f"\n\nRECURSION PATTERN SUMMARY\n\n"
    "Linear Recursion: One recursive call per level.\n"
    "Tail Recursion: Work occurs before the recursive call.\n"
    "Head Recursion: Work occurs after the recursive call.\n"
    "Increasing-Decreasing: Work occurs both before and after the call.\n"
    "Tree Recursion: Multi-branching calls that form a tree architecture.\n" # Summary text from the exemplar code
)
print(summary_text)
