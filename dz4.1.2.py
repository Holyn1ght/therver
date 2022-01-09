R = [1, 8, 11, 9]
G = [1, 5, 8, 6]
B = [3, 7, 11, 8]
RGB = [5, 20, 30, 23]

a = 41
c = 1
X0 = B[1]
m = 100
was = [-1 for i in range(m + 1)]
x = [X0]

was[X0] = 0
for i in range(1, 2 * m):
    now = (a * x[-1] + c) % m
    x.append(now)
    if was[now] != -1:
        print(f"Period is equal {i - was[now]}");
        break
    was[now] = i
for i in range(len(x)):
    print(f"{i} {x[i]}")

