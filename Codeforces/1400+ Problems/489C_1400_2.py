s, m = map(int, input().split())
isTrue = False
if s == 100:
    b_low = int("1".ljust(len(str(s)) + s - 3, "0"))
    b_high = int("9".ljust(len(str(s)) + s - 3, "9"))
elif s < 10:
    b_low = int("1".ljust(len(str(s)) + s - 1, "0"))
    b_high = int("9".ljust(len(str(s)) + s - 1, "9"))
else:
    b_low = int("1".ljust(len(str(s)) + s - 2, "0"))
    b_high = int("9".ljust(len(str(s)) + s - 2, "9"))
if s == 1 and m == 0:
    print(f"{0} {0}")
else:
    for i in range(s - 1, -1, -1):
        for n in range(1, 10):
            if sum(list(map(int, str(b_low)))) == m:
                break
            b_low = int(str(b_low)[:i] + str(n) + str(b_low)[i + 1:])
        if sum(list(map(int, str(b_low)))) == m:
            break
    for i in range(s - 1, -1, -1):
        for n in range(9, -1, -1):
            if sum(list(map(int, str(b_high)))) == m:
                isTrue = True
                break
            b_high = int(str(b_high)[:i] + str(n) + str(b_high)[i + 1:])
            if sum(list(map(int, str(b_high)))) == m and not sum(list(map(int, str(b_high)))) == 0:
                isTrue = True
                break
        if sum(list(map(int, str(b_high)))) == m:
            break
    if isTrue:
        print(f"{b_low} {b_high}")
    else:
        print(f"{-1} {-1}")

