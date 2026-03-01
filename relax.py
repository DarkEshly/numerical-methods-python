import math


def relax_method(m, f, n, w, e):
    iters = 0
    matrix = m[:]
    result = [0] * n
    delta = 1
    while delta >= e:
        iters += 1
        last_result = result[:]
        for i in range(0, n):
            first_sum = 0
            second_sum = 0
            for j in range(0, i):
                first_sum += matrix[i][j] * result[j]
            for j in range(i, n):
                second_sum += matrix[i][j] * last_result[j]
            result[i] = last_result[i] + w * (f[i] - first_sum -
                                              second_sum) / matrix[i][i]
        size = 0
        for i in range(0, n):
            size += (result[i] - last_result[i]) ** 2
        delta = math.sqrt(size)
    return result, iters


def by_formula(n, m, x):
    sp2, k = [], []
    Qm = 1.001 - 2 * m * (10 ** (-3))
    for i in range(1, n + 1):
        sp = []
        for j in range(1, n + 1):
            if j == i:
                sp.append((Qm - 1) ** (i + j))
            else:
                sp.append(Qm ** (i + j) + 0.1 * (j - i))
        k.append(x * math.e ** (x / i) * math.cos(x / i))
        sp2 += [sp]
    return sp2, k


def by_file(file_name):
    with open(file_name) as f:
        k = f.read().splitlines()
        b = [float(i.split()[-1]) for i in k]
        a = [list(map(float, (i.split())[:-1])) for i in k]
        return a, b


def main():
    flag = 0
    print('Как вы ходите создать матрицу, через файл или через формулу?')
    print('1 - через файл')
    print('2 - через формулу')
    a = input()
    matrix = []
    f = []
    while flag == 0:
        if a == '1':
            flag = 1
            file_name = ''
            while True:
                try:
                    print('Введите название файла')
                    file_name = input()
                    matrix, f = by_file(file_name)
                    break
                except:
                    print("Файла не существует или неверный формат файла")
            break
        if a == '2':
            flag = 1
            while True:
                try:
                    print('Введите значения n, m и x')
                    n, m, x = int(input()), float(input()), float(input())
                    break
                except:
                    print("Неверный формат данных")
            matrix, f = by_formula(n, m, x)
            break
        print('Неккоректный запрос')
        a = input()
    while True:
        try:
            print('Введите значения параметра w')
            w = float(input())
            break
        except:
            print("Неверный формат данных")
    while True:
        try:
            print('Введите значения точночти e')
            e = float(input())
            if e >= 1:
                print("Неверный формат данных")
            else:
                break
        except:
            print("Неверный формат данных")
    print('Введённая матрица A:')
    for i in range(len(f)):
        for j in range(len(f)):
            if j != len(f) - 1:
                print(matrix[i][j], ', ', sep='', end='')
            else:
                print(matrix[i][j])
    print('Введённый вектор f правой части::')
    for i in range(len(f)):
        print(f[i])
    print('Решение методом верхней релаксации:')
    solution, iters = relax_method(matrix, f, len(f), w, e)
    for i in range(len(solution)):
        if i == len(solution) - 1:
            print('x', i + 1, ' = ', solution[i], sep='')
        else:
            print('x', i + 1, ' = ', solution[i], end=', ', sep='')
    print('Число итераций =', iters)


main()