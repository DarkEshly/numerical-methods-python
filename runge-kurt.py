import math
import matplotlib.pyplot as plt
import decimal

decimal.getcontext().prec = 18


def first(x, y):
    return (y - y ** 2) * x


def second(x, u, v):
    return x + u - v ** 2 + 2


def third(x, u, v):
    return math.sin(x - u) + 2.1 * v


def fourth(x, y):
    return math.cos(x) ** 2


def fifth(x, u, v):
    return u + 2 * v


def sixth(x, u, v):
    return u - 5 * math.sin(x)


def runge_kutta(f, current_x, current_y, delta, n):
    x_points = [current_x]
    y_points = [current_y]
    h = delta / n
    for i in range(0, n):
        current_y += (h / 2) * (f(current_x,
                                  current_y) + f(current_x + h,
                                                 current_y +
                                                 h * f(current_x, current_y)))
        current_x = float(decimal.Decimal(str(current_x))
                          + decimal.Decimal(str(h)))
        x_points.append(current_x)
        y_points.append(current_y)
    return x_points, y_points


def runge_kutta_fourth_order(f, current_x, current_y, delta, n):
    x_points = [current_x]
    y_points = [current_y]
    h = delta / n
    for i in range(0, n):
        k1 = f(current_x, current_y)
        k2 = f(current_x + h / 2, current_y + k1 * h / 2)
        k3 = f(current_x + h / 2, current_y + k2 * h / 2)
        k4 = f(current_x + h, current_y + k3 * h)
        current_y += (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        current_x = float(decimal.Decimal(str(current_x))
                          + decimal.Decimal(str(h)))
        x_points.append(current_x)
        y_points.append(current_y)
    return x_points, y_points


def runge_kutta_system(fs, current_x, current_ys, delta, n):
    x_points = [current_x]
    y_points1 = [current_ys[0]]
    y_points2 = [current_ys[1]]
    h = delta / n
    for i in range(0, n):
        for j in range(0, 2):
            first_part = fs[j](current_x, current_ys[0], current_ys[1])
            second_part = fs[j](current_x + h,
                                current_ys[0] +
                                h * first_part, current_ys[1] + h * first_part)
            current_ys[j] += (first_part + second_part) * h / 2
        current_x = float(decimal.Decimal(str(current_x))
                          + decimal.Decimal(str(h)))
        x_points.append(current_x)
        y_points1.append(current_ys[0])
        y_points2.append(current_ys[1])
    return x_points, y_points1, y_points2


def runge_kutta_f_order_s(fs, current_x, current_ys, delta, n):
    x_points = [current_x]
    y_points1 = [current_ys[0]]
    y_points2 = [current_ys[1]]
    h = delta / n
    k1 = 2 * [0]
    k2 = 2 * [0]
    k3 = 2 * [0]
    k4 = 2 * [0]
    for i in range(0, n):
        k1[0] = fs[0](current_x, current_ys[0], current_ys[1])
        k1[1] = fs[1](current_x, current_ys[0], current_ys[1])
        k2[0] = fs[0](current_x + h / 2,
                      current_ys[0] + h / 2 * k1[0],
                      current_ys[1] + h / 2 * k1[1])
        k2[1] = fs[1](current_x + h / 2,
                      current_ys[0] + h / 2 * k1[0],
                      current_ys[1] + h / 2 * k1[1])
        k3[0] = fs[0](current_x + h / 2,
                      current_ys[0] + h / 2 * k2[0],
                      current_ys[1] + h / 2 * k2[1])
        k3[1] = fs[1](current_x + h / 2,
                      current_ys[0] + h / 2 * k2[0],
                      current_ys[1] + h / 2 * k2[1])
        k4[0] = fs[0](current_x + h,
                      current_ys[0] + h * k3[0],
                      current_ys[1] + h * k3[1])
        k4[1] = fs[1](current_x + h,
                      current_ys[0] + h * k3[0],
                      current_ys[1] + h * k3[1])
        current_ys[0] += h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        current_ys[1] += h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        current_x = float(decimal.Decimal(str(current_x)) +
                          decimal.Decimal(str(h)))
        x_points.append(current_x)
        y_points1.append(current_ys[0])
        y_points2.append(current_ys[1])
    return x_points, y_points1, y_points2


def main():
    flag = 0
    print('Выберите номер теста от 1 до 4, '
          'демонстрацию которого вы хотите просмотреть:')
    test = input()
    while flag == 0:
        if test == '1' or test == '2':
            if test == '1':
                print('Уравнение - dy/dx = (y - y^2) * x, y(0) = 3')
                print('Точное решение - 1 / (1 - 2 / 3 * e^(-1 / 2 * x ^ 2))')
            if test == '2':
                print('Уравнение - dy/dx = cos^2(x), y(0) = 5')
                print('Точное решение - sin(2x) / 4 + x / 2 + 5')
            flag = 1
            while True:
                try:
                    print('Введите значение параметра n')
                    n = int(input())
                    break
                except:
                    print("Неверный формат данных")
            order = ''
            while order != '1' and order != '2':
                print('Выберите порядок метода Рунга-Кутта:')
                print('1 - второй')
                print('2 - четвёртый')
                order = input()
                if order != '1' and order != '2':
                    print("Неверный формат данных")
            x_points = []
            y_points = []
            if order == '1':
                if test == '1':
                    x_points, y_points = runge_kutta(first, 0, 3, 1, n)
                if test == '2':
                    x_points, y_points = runge_kutta(fourth, 0, 5, 1, n)
            if order == '2':
                if test == '1':
                    x_points, y_points = runge_kutta_fourth_order(first, 0, 3,
                                                                  1, n)
                if test == '2':
                    x_points, y_points = runge_kutta_fourth_order(fourth, 0, 5,
                                                                  1, n)
            print('1. x 2. y приближ. 3. y точн.')
            for i in range(1, len(x_points)):
                if test == '1':
                    print('1.', x_points[i], '2.', y_points[i], '3.',
                          1 / (1 - 2 / 3 *
                               math.e ** (-1 / 2 * x_points[i] * x_points[i])))
                if test == '2':
                    print('1.', x_points[i], '2.', y_points[i], '3.',
                          math.sin(2 * x_points[i]) / 4 + x_points[i] / 2 + 5)
            if order == '1':
                plt.scatter(x_points, y_points, s=10, c='red')
                plt.plot(x_points, y_points, c='red', label='r-k')
            if order == '2':
                plt.scatter(x_points, y_points, s=10, c='red')
                plt.plot(x_points, y_points, c='red', label='r-k-4')
            x_points = []
            y_points = []
            current_x = 0
            current_y = 0
            for i in range(1000):
                x_points.append(current_x)
                if test == '1':
                    current_y = 1 / (1 - 2 / 3 *
                                     math.e ** (-1 / 2 * current_x * current_x))
                if test == '2':
                    current_y = math.sin(2 * current_x) / 4 + current_x / 2 + 5
                y_points.append(current_y)
                current_x += 1 / 1000
            plt.plot(x_points, y_points, c='blue', label='y(x)')
            plt.legend(fontsize=12)
            plt.grid(which='major')
            plt.show()
            break
        if test == '3':
            flag = 1
            print('Уравнение:')
            print('du / dx = x + u - v ^ 2 + 2')
            print('dv / dx = sin(x - u) + 2.1*v')
            print('u(0) = 1.5')
            print('v(0) = 0')
            while True:
                try:
                    print('Введите значение параметра n')
                    n = int(input())
                    break
                except:
                    print("Неверный формат данных")
            x_points, y1_points, y2_points = runge_kutta_system([second, third],
                                                                0, [1.5, 0], 1, n)
            print('Для метода Рунга-Кутта второго порядка:')
            print('1. x 2. u приближ. 3. v приближ.')
            for i in range(1, len(x_points)):
                print('1.', x_points[i], '2.', y1_points[i], '3.', y2_points[i])
            plt.scatter(x_points, y1_points, s=5, c='green')
            plt.scatter(x_points, y2_points, s=5, c='red')
            plt.plot(x_points, y1_points, c='green', label='r-k-u')
            plt.plot(x_points, y2_points, c='red', label='r-k-v')
            x_points, y1_points, y2_points = runge_kutta_f_order_s([second,
                                                                    third],
                                                                   0,
                                                                   [1.5, 0],
                                                                   1, n)
            print('Для метода Рунга-Кутта четвёртого порядка:')
            print('1. x 2. u приближ. 3. v приближ.')
            for i in range(1, len(x_points)):
                print('1.', x_points[i], '2.', y1_points[i], '3.', y2_points[i])
            plt.scatter(x_points, y1_points, s=5, c='purple')
            plt.scatter(x_points, y2_points, s=5, c='blue')
            plt.plot(x_points, y1_points, c='purple', label='r-k-4-u')
            plt.plot(x_points, y2_points, c='blue', label='r-k-4-v')
            plt.legend(fontsize=12)
            plt.grid(which='major')
            plt.show()
            break
        if test == '4':
            flag = 1
            print('Уравнение:')
            print('du / dx = u + 2v')
            print('dv / dx = u - 5sinx')
            print('u(0) = 3')
            print('v(0) = 2')
            print('Точное решение:')
            print('u = 3sinx - cosx + 8 / 3 * e ^ (2x) + 4 / 3 * e ^ (-x)')
            print('v = -sinx + 2cosx + 4 / 3 * e ^ (2x) - 4 / 3 * e ^ (-x)')
            while True:
                try:
                    print('Введите значение параметра n')
                    n = int(input())
                    break
                except:
                    print("Неверный формат данных")
            order = ''
            while order != '1' and order != '2':
                print('Выберите порядок метода Рунга-Кутта:')
                print('1 - второй')
                print('2 - четвёртый')
                order = input()
                if order != '1' and order != '2':
                    print("Неверный формат данных")
            x_points = []
            y1_points = []
            y2_points = []
            if order == '1':
                x_points, y1_points, y2_points = runge_kutta_system([fifth,
                                                                     sixth],
                                                                    0,
                                                                    [3, 2],
                                                                    1, n)
            if order == '2':
                x_points, y1_points, y2_points = runge_kutta_f_order_s([fifth,
                                                                        sixth],
                                                                       0, [3, 2],
                                                                       1, n)
            print('1. x 2. u приближ. 3. v приближ. 4. u точн. 5. v точн.')
            for i in range(1, len(x_points)):
                print('1.', x_points[i], '2.', y1_points[i], '3.', y2_points[i],
                      '4.',
                      3 * math.sin(x_points[i]) - math.cos(x_points[i]) +
                      8 / 3 * math.e ** (2 * x_points[i]) +
                      4 / 3 * math.e ** (-x_points[i]),
                      '5.', -math.sin(x_points[i]) +
                      2 * math.cos(x_points[i]) +
                      4 / 3 * math.e ** (2 * x_points[i]) -
                      4 / 3 * math.e ** (-x_points[i]))

            if order == '1':
                plt.scatter(x_points, y1_points, s=10, c='red')
                plt.scatter(x_points, y2_points, s=10, c='blue')
                plt.plot(x_points, y1_points, c='red', label='r-k-u')
                plt.plot(x_points, y2_points, c='blue', label='r-k-v')
            if order == '2':
                plt.scatter(x_points, y1_points, s=10, c='red')
                plt.scatter(x_points, y2_points, s=10, c='blue')
                plt.plot(x_points, y1_points, c='red', label='r-k-u-4')
                plt.plot(x_points, y2_points, c='blue', label='r-k-v-4')
            x_points = []
            y1_points = []
            y2_points = []
            current_x = 0
            current_y = 0
            for i in range(1000):
                x_points.append(current_x)
                current_y = 3 * math.sin(x_points[i]) - math.cos(x_points[i]) + \
                            8 / 3 * math.e ** (
                                    2 * x_points[i]) +\
                            4 / 3 * math.e ** (-x_points[i])
                y1_points.append(current_y)
                current_y = -math.sin(x_points[i]) + 2 * math.cos(x_points[i]) + \
                            4 / 3 * math.e ** (
                                    2 * x_points[i]) -\
                            4 / 3 * math.e ** (-x_points[i])
                y2_points.append(current_y)
                current_x += 1 / 1000
            plt.plot(x_points, y1_points, c='green', label='u(x)')
            plt.plot(x_points, y2_points, c='purple', label='v(x)')
            plt.legend(fontsize=12)
            plt.grid(which='major')
            plt.show()
            break
        print('Неверный формат ввода')
        print('Выберите номер теста от 1 до 4, '
          'демонстрацию которого вы хотите просмотреть:')
        test = input()


main()
