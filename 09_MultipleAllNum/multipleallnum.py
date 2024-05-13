def main():
    t = int(input())
    for i in range(t):
        multipleallnum()


def multipleallnum():
    s = str(input())
    while int(s) // 10:
        tmp = 1
        for x in s:
            if int(x): tmp *= int(x)
        s = str(tmp)
    print(s)

if __name__ == "__main__":
    main()
