def main():
    t = int(input())
    for i in range(t):
        inputs = input().split()
        n = int(inputs[0])
        data = list(map(int, inputs[1:]))
        k = int(input())
        y = []
        for x in range(n - k + 1):
            y.append(sum([data[num + x] for num in range(k)]) // k)
        print(n - k + 1, end=' ')
        for j in range(n - k + 1):
            print(y[j], end=' ')
        print()

if __name__ == "__main__":
    main()
