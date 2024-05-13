def main():
    testcase = int(input())
    for i in range(testcase):
        inputs = input().split()
        n = int(inputs[0])
        data = list(map(int, inputs[1:]))
        data_s = set(data)
        count = {}.fromkeys(data_s, 0)
        for x in data:
            if x in count:
                count[x] += 1
        key_list = sorted(count.keys())
        key_list.sort()
        for y in key_list:
            print(y,end=' ')
            print(count[y],end=' ')
        print()

if __name__ == '__main__':
    main()
