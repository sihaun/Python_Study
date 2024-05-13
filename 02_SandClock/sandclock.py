def main():
    t = int(input())
    for i in range(t):
        k = int(input()) # k = 7
        for l in range(k): # 3번 한 행에서의 행동 0~6
            h = k//2
            p = abs(abs(l-h)-h)
            if p <= h: bar(p)
            c=0
            for x in range(k-2*p):
                if c%2:
                    print('+',end='')
                    c+=1
                else:
                    print('*',end='')
                    c+=1
            if p <= h: bar(p)
            print()
def bar(n):
     for i in range(n):
        print('-',end='')

if __name__ == '__main__':
    main()