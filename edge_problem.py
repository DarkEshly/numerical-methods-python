import matplotlib.pyplot as plt
import decimal
import math
decimal.getcontext().prec = 18


def p1(x):
    return -3 * x


def q1(x):
    return 2


def f1(x):
    return -1.5


def p2(x):
    return 1


def q2(x):
    return 0


def f3(x):
    return 5


def edge_solution(p, q, f, a, b, sigma1, teta1, deta1, sigma2, teta2, deta2, n):
    h = (b - a) / n
    alpha_numbers = [0] * n
    betta_numbers = [0] * n
    alpha_numbers[0] = -(teta1 / (sigma1 * h - teta1))
    betta_numbers[0] = deta1 / (sigma1 - teta1 / h)
    current_x = a
    x_points = [0] * (n + 1)
    x_points[0] = current_x
    ys = [0] * (n + 1)
    for i in range(1, n):
        current_x = float(decimal.Decimal(str(current_x)) +
                          decimal.Decimal(str(h)))
        x_points[i] = current_x
        big_a = 1 / (h ** 2) - p(current_x) / (2 * h)
        big_b = 1 / (h ** 2) + p(current_x) / (2 * h)
        big_c = 2 / (h ** 2) - q(current_x)
        alpha_numbers[i] = big_b / (-big_a * alpha_numbers[i - 1] + big_c)
        betta_numbers[i] = (f(current_x) -
                            big_a * betta_numbers[i - 1]) / \
                           (big_a * alpha_numbers[i - 1] - big_c)
    ys[n] = (deta2 * h +
             teta2 * betta_numbers[n - 1]) / \
            (sigma2 * h + teta2 * (1 - alpha_numbers[n - 1]))
    x_points[n] = b
    for i in range(n - 1, -1, -1):
        ys[i] = ys[i + 1] * alpha_numbers[i] + betta_numbers[i]
    return x_points, ys


def main():
    flag = 0
    print('Выберите номер теста от 1 до 3, '
          'демонстрацию которого вы хотите просмотреть:')
    test = input()
    while flag == 0:
        if test == '1':
            flag = 1
            print('Дана следующая система:')
            print("y'' - 3xy' + y = x")
            print("y'(0.7) = 1.3")
            print("0.5y(1) + y'(1) = 2")
            while True:
                try:
                    print('Введите значение параметра n')
                    n = int(input())
                    break
                except:
                    print("Неверный формат данных")
            x_points, y_points = edge_solution(p1, q1, f1, 0.7,
                                               1, 0, 1, 1.3, 0.5, 1, 2, n)
            print('1. x 2. y')
            for i in range(len(x_points)):
                print('1.', x_points[i], '2.', y_points[i])
            plt.scatter(x_points, y_points, s=10, c='red')
            plt.plot(x_points, y_points, c='red', label='y.')
            plt.legend(fontsize=12)
            plt.grid(which='major')
            plt.show()
            break
        if test == '2':
            flag = 1
            print('Дана следующая система:')
            print("y'' + y' = 1")
            print("y'(0) = 0")
            print("y(1) = 1")
            print('Точное решение:')
            print("y = x + e^(-x) - 1/e")
            while True:
                try:
                    print('Введите значение параметра n')
                    n = int(input())
                    break
                except:
                    print("Неверный формат данных")
            x_points, y_points = edge_solution(p2, q2, p2, 0, 1,
                                               0, 1, 0, 1, 0, 1, n)
            print('1. x 2. y приближ. 3. y точн.')
            for i in range(len(x_points)):
                print('1.', x_points[i], '2.', y_points[i], '3.',
                      x_points[i] + math.e ** (-x_points[i]) - 1 / math.e)
            plt.scatter(x_points, y_points, s=10, c='red')
            plt.plot(x_points, y_points, c='red', label='y-приб.')
            x_points = []
            y_points = []
            current_x = 0
            current_y = 0
            for i in range(1000):
                x_points.append(current_x)
                current_y = x_points[i] + math.e ** (-x_points[i]) - 1 / math.e
                y_points.append(current_y)
                current_x += 1 / 1000
            plt.plot(x_points, y_points, c='blue', label='y-точн.')
            plt.legend(fontsize=12)
            plt.grid(which='major')
            plt.show()
            break
        if test == '3':
            flag = 1
            print('Дана следующая система:')
            print("y'' + y' = 5")
            print("y(0) = 1")
            print("y'(1) = 5")
            print('Точное решение:')
            print("y = 5x + 1")
            while True:
                try:
                    print('Введите значение параметра n')
                    n = int(input())
                    break
                except:
                    print("Неверный формат данных")
            x_points, y_points = edge_solution(p2, q2, f3, 0, 1,
                                               1, 0, 1, 0, 1, 5, n)
            print('1. x 2. y приближ. 3. y точн.')
            for i in range(len(x_points)):
                print('1.', x_points[i], '2.', y_points[i], '3.',
                      5 * x_points[i] + 1)
            plt.scatter(x_points, y_points, s=10, c='red')
            plt.plot(x_points, y_points, c='red', label='y-приб.')
            x_points = []
            y_points = []
            current_x = 0
            current_y = 0
            for i in range(1000):
                x_points.append(current_x)
                current_y = 5 * x_points[i] + 1
                y_points.append(current_y)
                current_x += 1 / 1000
            plt.plot(x_points, y_points, c='blue', label='y-точн.')
            plt.legend(fontsize=12)
            plt.grid(which='major')
            plt.show()
            break
        print('Неверный формат ввода')
        print('Выберите номер теста от 1 до 3, '
              'демонстрацию которого вы хотите просмотреть:')
        test = input()


main()

