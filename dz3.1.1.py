import matplotlib.pyplot as plt

R = [1, 8, 11, 9]
G = [1, 5, 8, 6]
B = [3, 7, 11, 8]
RGB = [5, 20, 30, 23]

Tc = R[1]
print(Tc)
Ts = G[1] + B[1] + RGB[2]
print(Ts)

l = 1 / Tc      # интенсивность потока заявок
m = 1 / Ts      # интенсивность потока обслуживания
p = l / m
A = [1] #       1,      p,              p^2,                p^3,        p^4, ...
P0 = [1] #      1 / 1,  1 / (1 + p),    1 / (1 + p + p^2), ...

sum = A[0]

for i in range(1, 20):
    A.append(A[-1] * p / i)
    sum += A[-1]
    P0.append(1 / sum)

n = 0

while A[n] * P0[n] > 0.01:
    n += 1
print(n)


def otk(n):
    x = [i for i in range(n + 1)]
    y = [A[i] * P0[i] for i in x]
    plt.title("P отк")  # заголовок
    plt.xlabel("n")  # ось абсцисс
    plt.ylabel("P")  # ось ординат
    plt.grid()  # включение отображение сетки
    plt.bar(x, y)
    plt.show()


B = []


def busy(n):
    x = [i for i in range(n + 1)]
    y = []
    for i in x:
        sm = 0
        for j in range(i + 1):
            sm += A[j] * P0[i] * j
        B.append(sm)
    plt.title("M зан")  # заголовок
    plt.xlabel("n")  # ось абсцисс
    plt.ylabel("M")  # ось ординат
    plt.grid()  # включение отображение сетки
    plt.bar(x, B)
    plt.show()


def zagr(n):
    x = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        B[i] /= i
    plt.title("K загр")  # заголовок
    plt.xlabel("n")  # ось абсцисс
    plt.ylabel("K")  # ось ординат
    plt.grid()  # включение отображение сетки
    plt.bar(x, B)
    plt.show()


otk(n)
busy(n)
zagr(n)

    # x = []
    # y = []
    #
    # plt.title("P(3 <= k)")  # заголовок
# plt.xlabel("n")  # ось абсцисс
# plt.ylabel("P(k)")  # ось ординат
# plt.grid()  # включение отображение сетки
# plt.plot(x, y)
# plt.show()