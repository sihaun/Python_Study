def main():
    t = int(input())
    for i in range(t):
        m, n = map(int, input().split())
        print(int(n*(n+1)/2 - m*(m-1)/2))
if __name__ == '__main__':
    main()