input("Head tail - head is lst[0] tail is lst[1:] base case is []. Press Enter: ")
print(" [10, 20, 30] head:", [10, 20, 30][0], " tail:", [10,20,30][1:])
print(" [5, 15, 35] head:", [5, 15, 35][0], "tail:", [5, 15, 35][1:])

lst = [int(x) for x in input("Enter three numbers seperated by spaces: ").split()]
guess = input("What is the head of " + str(lst) + "?")
input("Head of lst[0] tail is lst[1:]. Press Enter: ")
print(" head:", lst[0], " your guess:", guess)