taskcase = int(input())
for i in range(taskcase):
    trisize = int(input())
    b = 1
    for j in range(1, trisize + 1):
        num = b
        p = trisize - 1
        for x in range(j):
            print(num, end=" ")
            num += p
            p -= 1
        b += 1
        print()
