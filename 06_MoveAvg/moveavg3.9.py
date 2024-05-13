def main():
    t = int(input())
    for i in range(t):
        inputs = input().split()
        n = int(inputs[0])
        data = list(map(int, inputs[1:]))
        k = int(input())
        y = []         
        d_sum = sum(data[:k])
        y.append(d_sum // k)
        for num in range(1, n - k + 1):
            d_sum = d_sum - data[num - 1] + data[num + k - 1]
            y.append(d_sum // k)
        print(n - k + 1, end=' ')
        for value in y:
            print(value, end=' ')
        print()

if __name__ == "__main__":
    main()
