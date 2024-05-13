def main():
    t = int(input())
    for i in range(t):
        fdata = map(str, input().split()[1:])
        calendnum(fdata)

def calendnum(l):
    tmp = 1
    for x in l:
        tmp *= int(x[-1])
        tmp = int(str(tmp)[-1])
    print(tmp)

if __name__ == "__main__":
    main()
