def stair_ways(n): # the recursive function
    if n == 0:
        return 1
    if n < 0:
        return 0
    return stair_ways(n - 1) + stair_ways(n - 2) # recursive steps taken

stairs = 5
print("Number of stairs:", stairs)
print("Total ways to climb:", stair_ways(stairs))


def trace_stair_ways(n, space=""):
    print(f"{space}stair_ways({n})")
    if n == 0:
        print(f"{space}Reached 0 stairs -> return 1")
        return 1
    if n < 0:
        print(f"{space}Went below 0 stairs -> return 0")
        return 0
    one_step = trace_stair_ways(n - 1, space + " ")
    two_steps = trace_stair_ways(n - 2, space + " ")
    total = one_step + two_steps
    print(f"{space}Total ways for {n} stairs = {total}")
    return total

trace_stair_ways(3)

def generate_braces(current, open_count, close_count, total_pairs):
    if len(current) == total_pairs * 2:
        print(current)
        return
    if open_count < total_pairs:
        generate_braces(current + "{", open_count + 1, close_count, total_pairs)
    if close_count < open_count:
        generate_braces(current + "}", open_count, close_count + 1, total_pairs)

pairs = 3
print("Number of pairs:", pairs)
generate_braces("", 0, 0, pairs)
