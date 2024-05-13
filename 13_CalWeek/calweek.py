GREGORIAN = 1582

def main():
    t = int(input())
    for i in range(t):
        year, month, day = map(int, input().split(" "))
        print(getDateOfWeek(year,month,day))

def getDateOfWeek(year, month, day):
    mday = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = 0
    for pyear in range(GREGORIAN,year):
        if pyear % 400 == 0 or (pyear % 4 == 0 and pyear % 100 != 0):
            date += 1
        date += 365
    for pmonth in range(month-1):
        if pmonth == 1 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            date += 1
        date += mday[pmonth]
    date += day-1

    return (date + 5) % 7


if __name__ == "__main__":
    main()