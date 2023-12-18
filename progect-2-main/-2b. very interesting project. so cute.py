def print_pascal_triangle(n):
    if n < 0:
        print("Ошибка: Число n должно быть неотрицательным.")
        return

    for line in range(n):
        # Для каждой строки создаем первое число равное 1
        C = 1
        for i in range(1, line + 1):
            print(C, end=" ")

            # Вычисление значения следующего числа в строке
            # Используем формулу биномиальных коэффициентов C(line, i) = C(line, i-1) * (line - i + 1) / i
            C = C * (line - i + 1) // i

        print("1")  # Каждая строка заканчивается на 1


# Считываем значение n
n = int(input("Введите целое число n для вывода n первых строчек треугольника Паскаля: "))

print_pascal_triangle(n)


def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""

    start = 0
    end = 0

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)  # палиндром нечетной длины
        len2 = expand_around_center(s, i, i + 1)  # палиндром четной длины
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def expand_around_center(s, left, right):
    L, R = left, right

    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1

    return R - L - 1


s = input("Введите строку: ")
print(longest_palindromic_substring(s))

# Считываем значения n, m, k, h
n, m, k, h = map(int, input().strip().split())

# Проверяем возможность умножения
if m != k:
    print("Ошибка: Матрицы нельзя перемножить из-за несоответствия размеров.")
else:
    # Считываем матрицу A
    A = []
    for i in range(n):
        A.append(list(map(int, input().strip().split())))

    # Считываем матрицу B
    B = []
    for j in range(k):
        B.append(list(map(int, input().strip().split())))

    # Инициализируем матрицу C размером n x h
    C = [[0 for _ in range(h)] for _ in range(n)]

    # Вычисляем произведение матриц A и B, записываем результат в C
    for i in range(n):
        for j in range(h):
            for t in range(m):  # или m or k, они равны
                C[i][j] += A[i][t] * B[t][j]

    # Выводим матрицу C
    for row in C:
        print(' '.join(map(str, row)))
