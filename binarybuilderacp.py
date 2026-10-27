# More or less same function as exemplar code   

items = ["A", "B", "C"]
n = len(items)
total_subsets = 1 << n # easier way to calcuate

print(f"\nBINARY SUBSET BUILDER\n")
print(f"Items: {items}\nNumber of items: {n}\nTotal subsets: 2 ^ {n} = {total_subsets}\n")

print("--- PART 1 & 2: Power Set & Binary Mask Table ---")
for mask in range(total_subsets):
    bits = [f"[{items[j]}]={(mask >> j) & 1}" for j in range(n-1, -1, -1)]
    print(f"Mask {mask:2d} -> " + " ".join(bits))

print("\n--- PART 3: Bit Probe ---")
sample_mask = 5  
print(f"Sample Mask: {sample_mask} (Binary: {bin(sample_mask)})")
for j, item in enumerate(items):
    is_set = (sample_mask & (1 << j)) != 0
    status = "is set, so item selected" if is_set else "is not set, so item skipped"
    print(f"  Bit {j}: {status} -> {item}")

print("\n--- PART 4: All Subsets ---")
for mask in range(total_subsets):
    subset = [items[j] for j in range(n) if mask & (1 << j)]
    print(f"Mask {mask:2d} -> {subset}")

def bit_difference(a, b):
    return (a ^ b).bit_count()

print("\n--- PART 5: Bit Difference ---")
for a, b in [(12, 15), (21, 24), (8, 8)]:
    print(f"Diff between {a} and {b}: {bit_difference(a, b)} | ({bin(a)} vs {bin(b)})")

summary_text = (
    f"\nBINARY SUBSET BUILDER SUMMARY\n\n"
    "Power Set: All possible subsets of a set.\n"
    "Binary Mask: A number that selects items using bits.\n"
    "Bit Probe: Uses 1 << j to check a specific bit.\n"
    "Two Loops: One loop for masks, one loop for items.\n"
    "Bit Difference: Counts different bit positions via XOR (^).\n"
)
print(summary_text)