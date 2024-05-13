def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(checksum(n))

def checksum( num):
    mask = 0x000000ff
    s = []
    for i in range(4):
        s.append((num & mask) >> 8*i)
        mask <<= 8
    nsum = sum(s,-s[0])
    while nsum > 255 : nsum -= 256
    if (255-nsum) == s[0]: return 1
    else : return 0

if __name__ == "__main__":
    main()
