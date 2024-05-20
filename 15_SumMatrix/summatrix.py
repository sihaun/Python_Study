def summatrix(m1, m2):
    for d1, d2 in zip(m1, m2):
        for c1, c2 in zip(d1, d2):
            print(c1 + c2, end=' ')
        print()

def main():
    t = int(input())
    for i in range(t):
        r, c = map(int, input().split())
        mat1 = []
        mat2 = []
        for j in range(r):
            mat1.append(list(map(int, input().split())))
        for k in range(r):
            mat2.append(list(map(int, input().split())))
        summatrix(mat1, mat2)

if __name__ == "__main__":
    main()
