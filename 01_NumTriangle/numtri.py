def main():
    t = int(input())
    for i in range(t):
        k = int(input())
        b = 1
        for j in range(k):
            num = b
            p = k-1
            for x in range(j+1):
                print(num, end=" ")
                num += (p)
                p -=1
            b += 1
            print()
if __name__ == '__main__':
    main()
