def main():
    t = int(input())
    for i in range(t):
        inps = input().split()
        data = list(map(int, inps[1:]))
        zero = 0
        p = 1
        for n in data:
            while n % 10 == 0:
                n //= 10
                zero += 1          
            p *= n
            while (p) % 10 == 0:
                p //= 10
                zero += 1

        print(f"{p%10} {zero}")

if __name__ == "__main__":
    main()