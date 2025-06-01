size = int(input("Enter the size of the pattern:"))

i = 0
while i < size:
    #print("*")
    j=0
    for j in range(size):
        print("*", end ="")
    print("")
    i += 1