import math


def infinite_norm(matrix, n):
    b = [0] * n
    for i in range(0, n):
        for j in range(0, n):
            b[i] += abs(matrix[j][i])
    maxi = b[0]
    for i in range(1, n):
        if b[i] > maxi:
            maxi = b[i]
    return maxi


def condition_number(matrix, n):
    return infinite_norm(matrix, n) * infinite_norm(inverted_matrix(matrix, n), n)


def det(m, n):
    matrix = m[:]
    result = 1
    for i in range(0, n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    help_line = matrix[j][:]
                    matrix[j] = matrix[i][:]
                    matrix[i] = help_line[:]
                    result *= -1
                    break
        result *= matrix[i][i]
        matrix[i] = [x / matrix[i][i] for x in matrix[i]]
        for j in range(i + 1, n):
            matrix[j] = [x - y * matrix[j][i] for
                         x, y in zip(matrix[j], matrix[i])]
    return result


def inverted_matrix(m, n):
    result = [[0 for i in range(n)] for j in range(n)]
    matrix = m[:]
    for i in range(0, n):
        result[i][i] = 1
    for i in range(0, n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    help_line = matrix[j][:]
                    matrix[j] = matrix[i][:]
                    matrix[i] = help_line[:]
                    c = result[i]
                    result[i] = result[j]
                    result[j] = c
                    break
        result[i] = [x / matrix[i][i] for x in result[i]]
        matrix[i] = [x / matrix[i][i] for x in matrix[i]]
        for j in range(i + 1, n):
            result[j] = [x - y * matrix[j][i] for
                         x, y in zip(result[j], result[i])]
            matrix[j] = [x - y * matrix[j][i] for
                         x, y in zip(matrix[j], matrix[i])]
    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            result[j] = [x - y * matrix[j][i] for
                         x, y in zip(result[j], result[i])]
            matrix[j] = [x - y * matrix[j][i] for
                         x, y in zip(matrix[j], matrix[i])]
    return result


def gauss_straight_way(matrix, f, n):
    for i in range(0, n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] != 0:
                    help_line = matrix[j][:]
                    matrix[j] = matrix[i][:]
                    matrix[i] = help_line[:]
                    c = f[i]
                    f[i] = f[j]
                    f[j] = c
                    break
        f[i] /= matrix[i][i]
        matrix[i] = [x / matrix[i][i] for x in matrix[i]]
        for j in range(i + 1, n):
            f[j] -= matrix[j][i] * f[i]
            matrix[j] = [x - y * matrix[j][i] for
                         x, y in zip(matrix[j], matrix[i])]


def gauss_with_main(matrix, f, n):
    for i in range(0, n):
        current_elem = matrix[i][i]
        for j in range(i + 1, n):
            if matrix[j][i] > current_elem:
                help_line = matrix[j][:]
                matrix[j] = matrix[i][:]
                matrix[i] = help_line[:]
                current_elem = matrix[j][i]
                c = f[i]
                f[i] = f[j]
                f[j] = c
        f[i] /= matrix[i][i]
        matrix[i] = [x / matrix[i][i] for x in matrix[i]]
        for j in range(i + 1, n):
            f[j] -= matrix[j][i] * f[i]
            matrix[j] = [x - y * matrix[j][i] for
                         x, y in zip(matrix[j], matrix[i])]


def gauss_backward_way(matrix, f, n):
    result = n * [0]
    for i in range(n - 1, -1, -1):
        summ = 0
        for j in range(i + 1, n):
            summ += result[j] * matrix[i][j]
        result[i] = f[i] - summ
    return result


def gauss(m, fa, n, mode):
    matrix = m[:]
    f = fa[:]
    if mode == 0:
        gauss_straight_way(matrix, f, n)
    else:
        gauss_with_main(matrix, f, n)
    result = gauss_backward_way(matrix, f, n)
    return result


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


def by_test_formula(n):
    sp2, k = [], []
    for i in range(1, n + 1):
        sp = []
        for j in range(1, n + 1):
            sp.append(1 / (i + j - 1))
        k.append(i)
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
    print('2 - через формулу из варианта')
    print('3 - через формулу из теста a_ij = 1 / (i + j - 1), f_i = i')
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
        if a == '3':
            flag = 1
            while True:
                try:
                    print('Введите значение n')
                    n = int(input())
                    break
                except:
                    print("Неверный формат данных")
            matrix, f = by_test_formula(n)
            break
        print('Неккоректный запрос')
        a = input()
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
    print('Решение методом Гаусса:')
    solution = gauss(matrix, f, len(f), 0)
    count = 1
    for i in range(len(solution)):
        if i == len(solution) - 1:
            print('x', i + 1, ' = ', solution[i], sep='')
        else:
            print('x', i + 1, ' = ', solution[i], end=', ', sep='')
        if count == 4:
            print('')
            count = 0
        count += 1
    print('Решение методом Гаусса с выбором главного элемента:')
    solution = gauss(matrix, f, len(f), 1)
    count = 1
    for i in range(len(solution)):
        if i == len(solution) - 1:
            print('x', i + 1, ' = ', solution[i], sep='')
        else:
            print('x', i + 1, ' = ', solution[i], end=', ', sep='')
        if count == 4:
            print('')
            count = 0
        count += 1
    print('Определитель det(A) =', det(matrix, len(f)))
    print('Обратная матрицы:')
    inv_matrix = inverted_matrix(matrix, len(f))
    for i in range(len(f)):
        for j in range(len(f)):
            if j != len(f) - 1:
                print(inv_matrix[i][j], ', ', sep='', end='')
            else:
                print(inv_matrix[i][j])
    print("Число обусловленности матрицы: ", condition_number(matrix, len(f)))


main()

