def main():
    t = int(input())
    for i in range(t):
        n = str(input())
        print(multipleofelev(n))

def multipleofelev(lit):
    result = ""
    if len(lit) == 1: return 0
    while len(lit) > 1:
        front = int(lit[:-1])
        back = int(lit[-1])
        result += str(back)
        if front - back < 0:
            return 0
        else :
            lit = str(front - back)
    if lit == "0":
        return result[::-1]
    else :
        return 0

if __name__ == "__main__":
    main()
