N = int(input("Введите количество строк паскаля"))
if N <= 0:  # блюдим за некорректным вводом
    print('sorry, wrong input.')
else:
    P = []

    for i in range(N):
        row = [1] * (i + 1)  # формеруем текущую строку паскаля
        for j in range(i + 1):
            if j != 0 and j != i:  # "отсекаем" одинички по краям
                row[j] = P[i - 1][j - 1] + P[i - 1][j]  # формируем промежуточные значения
        P.append(row)

    for r in P:  # выводим все по красоте
        print(r)
