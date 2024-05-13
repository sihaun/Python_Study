def main():
    for i in range(int(input())):
        n, *data = map(int, input().split())
        data_s = set(data)
        count = {}.fromkeys(data_s, 0)
        for x in data:
            if x in count:
                count[x] += 1
        key_list = list(count.keys())
        key_list.sort()
        for y in key_list:
            print(y,end=' ')
            print(count[y],end=' ')
        print()

if __name__ == '__main__':
    main()
            
            