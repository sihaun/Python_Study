def main():
    for t in range(int(input())):
        k = int(input())
        mid = k//2
        for i in range(k):
            for j in range(k):
                if i == mid and j == mid:
                    print("O",end='')
                elif i == mid:
                    print("+",end='')
                elif j == mid:
                    print("I",end='')
                elif i+j == k-1:
                    print("*",end='')
                else:
                    print(".",end='')
            print()
if __name__ == "__main__":
    main()