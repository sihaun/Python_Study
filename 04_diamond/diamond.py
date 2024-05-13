def main():
    t = int(input())
    for i in range(t):
        k = int(input())
        for l in range(k):
            h = int(k/2)
            p = abs(l-h)
            if p <= h: star(p)
            c=0
            for x in range(k - 2 * p):
                print('+',end='')
            if p <= h: star(p)
            print()
def star(n):
    for i in range(n):
        print('*',end='')
if __name__ == '__main__':
    main()