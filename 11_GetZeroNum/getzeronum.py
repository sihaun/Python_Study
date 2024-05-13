def main():
    t = int(input())
    for i in range(t):
        fdata = map(int, input().split()[1:])
        countzero(fdata)
def countzero(l):
    k = 1
    count = 0
    for x in l:
        k *= x
        while k % 10 == 0:
            k //= 10
            count += 1
    print(count)
if __name__ == "__main__":
    main()