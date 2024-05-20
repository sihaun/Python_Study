def multimatrix(m1, m2, r, s, t):
    for y in range(r):
        for x in range(t):
            total = 0
            for z in range(s):
                total += m1[y][z] * m2[z][x]
            print(total, end=' ')
        print()

def main():
    testcase = int(input())
    for _ in range(testcase):
        r, s, t = map(int, input().split())
        mat1 = []
        mat2 = []
        for _ in range(r):
            mat1.append(list(map(int, input().split())))
        for _ in range(s):
            mat2.append(list(map(int, input().split())))
        multimatrix(mat1, mat2, r, s, t)

if __name__ == "__main__":
    main()
