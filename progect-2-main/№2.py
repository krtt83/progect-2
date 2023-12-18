def lp(str):
    n = len(str)
    maxlen = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            f = 1
            for k in range(0, ((j - i) // 2) + 1):
                if (str[i + k] != str[j - k]):
                    f = 0
            if (f != 0 and (j - i + 1) > maxlen):
                start = i
                maxlen = j - i + 1
    return maxlen


s = input("Bведите строку")
print(lp(s))
