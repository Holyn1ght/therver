
import matplotlib.pyplot as plt

LAMBDA = 1/5
MU = 1/36
eps = 0.000001
V = 1 / 75

def main():
    # Вычисление n
    n = 0  # n - количество операторов
    sump = 1
    p = []  # массив с вероятностями
    p.append(1)

    while p[0] * p[n] > 0.00999999:
        n += 1
        p.append(LAMBDA / MU * p[n - 1] / n)
        sump += p[n]
        p[0] = 1 / sump



    xn = [] # для проставления значений на оси абсцисс
    y3M = [] # мат ожидание количества занятых операторов
    y3Z = [] # коэффициент загрузки операторов
    y3q = [] # вероятность появления очереди
    y3MQ = [] # мат ожидание количества занятых мест в очереди
    n0 = 1 # нижняя граница количества операторов
    p[0] = 1

    for i in range(1, n + 1):
        p[i] = p[i - 1] * LAMBDA / i / MU

    while (LAMBDA / n0 / MU > 1): # определяем нижнюю границу количества операторов
        n0 += 1

    for n1 in range(n0, n + 1):
        sump2 = 1 # знаменатель Po
        a = LAMBDA / n1 / MU
        for i in range(1, n1):
            sump2 += p[i]
        sump2 += p[n1] / (1 - a)
        p[0] = 1 / sump2
        M = 0
        for i in range(1, n1):
            M += p[i] * i * p[0]
        M += p[n1] * p[0] * n1 / (1 - a)
        MQ = p[n1] * p[0] * a / (1 - a) ** 2
        y3M.append(M)
        y3Z.append(M / n1)
        y3q.append(p[n1] * p[0] * a / (1 - a))
        y3MQ.append(MQ)
        xn.append(n1)
        """
    plt.figure("Математическое ожидание количества занятых операторов")
    plt.title("Задание 1.3")
    plt.plot(xn, y3M)
    plt.figure("Коэффициент загруженности операторов")
    plt.title("Задание 1.3")
    plt.plot(xn, y3Z)
    plt.figure("Вероятность появления очереди")
    plt.title("Задание 1.3")
    plt.plot(xn, y3q)
    plt.figure("Математическое ожидание длины очереди")
    plt.title("Задание 1.3")
    plt.plot(xn, y3MQ)
    plt.show()
"""
    xn = []
    y4M = []
    y4Z = []
    y4q = []
    y4MQ = []
    p[0] = 1
    for i in range(1, n + 1):
        p[i] = p[i - 1] * LAMBDA / i / MU
    for n1 in range(1, n + 1):
        sump = 1
        for i in range(1, n1 + 1):
            sump += p[i]
        past_p0 = 100
        p[0] = 1 / sump
        m = 0
        next_p = p[n1]
        pp = []
        sump2 = 0
        while abs(p[0] - past_p0) > eps:
            m += 1
            next_p *= LAMBDA / (n1 * MU + V * m)
            pp.append(next_p)
            sump2 += next_p
            print(sump2)
            past_p0 = p[0]
            p[0] = 1 / (sump2 + sump)
            #print(p[0])
        M = 0
        #print(p[0])
        for i in range(1, n1 + 1):
            M += p[i] * p[0] * i
        M += p[0] * n1 * sump2
        MQ = 0
        for i in range(0, m):
            MQ += p[0] * pp[i] * (i + 1)
        y4M.append(M)
        y4Z.append(M / n1)
        y4q.append(sump2 * p[0])
        y4MQ.append(MQ)
        xn.append(n1)
        """
    plt.figure("Математическое ожидание количества занятых операторов")
    plt.title("Задание 1.4")
    plt.plot(xn, y4M)
    plt.figure("Коэффициент загруженности операторов")
    plt.title("Задание 1.4")
    plt.plot(xn, y4Z)
    plt.figure("Вероятность появления очереди")
    plt.title("Задание 1.4")
    plt.plot(xn, y4q)
    plt.figure("Математическое ожидание длины очереди")
    plt.title("Задание 1.4")

    plt.plot(xn, y4MQ)
    plt.show()
    #"""
    #"""
    LAMBDA2 = 1 / 68
    MU2 = 1 / 24
    N2 = 44
    """LAMBDA2 = 1 / 75
    MU2 = 1 / 26
    N2 = 49"""
    """
    p = [1 for i in range(N2 + 1)]
    xk = []
    yMN = []
    yMQ = []
    ypq = []
    yMK = []
    yMKZ = []
    for k in range(1, N2 + 1):
        p[k] = (N2 - k + 1) * LAMBDA2 / k / MU2 * p[k - 1]
        sump = 1
        for i in range(1, k + 1):
            sump += p[i]
        for i in range(k + 1, N2 + 1):
            p[i] = p[i - 1] * LAMBDA2 / k / MU2 * (N2 - i + 1)
            sump += p[i]
        p[0] = 1 / sump
       # print(p[0])
        MN = 0
        for i in range(0, N2):
            MN += (N2 - i) * p[i] * p[0]
        yMN.append(N2 - MN)
        MQ = 0
        for i in range(k + 1, N2 + 1):
            MQ += (i - k) * p[i] * p[0]
        yMQ.append(MQ)
        s = 0
        for i in range(k + 1, N2 + 1):
            s += p[i] * p[0]
        ypq.append(s)
        MK = 0
        for i in range(1, k + 1):
            MK += i * p[i] * p[0]
        for i in range(k + 1, N2 + 1):
            MK += k * p[i] * p[0]
        yMK.append(MK)
        yMKZ.append(MK / k)
        xk.append(k)

    plt.figure("Математическое ожидание числа простаивающих станков")
    plt.title("Задание 2")
    plt.plot(xk, yMN)
    plt.figure("Математическое ожидание числа станков, ожидающих обслуживания")
    plt.title("Задание 2")
    plt.plot(xk, yMQ)
    plt.figure("Вероятность ожидания обслуживания")
    plt.title("Задание 2")
    plt.plot(xk, ypq)
    plt.figure("Математическое ожидание числа занятых наладчиков")
    plt.title("Задание 2")
    plt.plot(xk, yMK)
    plt.figure("Коэффициент занятости наладчиков")
    plt.title("Задание 2")
    plt.plot(xk, yMKZ)
    plt.show()
"""
if __name__ == '__main__':
    main()
