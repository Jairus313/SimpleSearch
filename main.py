

n = input("enter the paragraph")

n = n.split()

m = input("enter the word for searching")

if m in n:
    print("yes!Its there :)")
    print("do wanna where it is:y/n?")

    a = input()

    if a == "y":
        print("the place is", end=" ")
        print(n.index(m) + 1)
        print("thank you")

    else:
        print("thank you")

else:
    print("Not there!")



