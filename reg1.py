import math
# [f_sr, f_niz, f_verh, L_sign_i, L_shum_i, k_niz_i, k_verh_i, k_i, d_A_i, E_f_i, w_i, A_i]

"""
Обыкновенная филенчатая дверь без прокладок 14 16 22 22 20
                              с прокладками 19 23 30 33 32
"""

data = [[250, 175, 355, 58, 30],
        [500, 355, 710, 58, 30],
        [1000, 710, 1400, 53, 25],
        [2000, 1400, 2800, 48, 25],
        [4000, 2800, 5600, 45, 25]]



Q_per = 12.5 * math.log(47, 10) + 14

Q_door = [Q_per for i in range(5)]

Q_per = 0
Q_door = [30, 39, 42, 45, 43]

print("Коэффициент веса каждой i-ой октавной полосы частот k_i:")
print("k_i = k_верх - k_нижн")

A = 0

for i in range(5):
    fa = data[i]
    print("f_ср. = ", fa[0])
    if 100 < fa[2] < 400:
        k_up = 2.57 * pow(10, -8) * pow(fa[2], 2.4)
    elif 400 < fa[2] < 10000:
        k_up = 1 - 1.074 * math.exp(pow(-10, -4) * pow(fa[2], 1.18))

    if 100 < fa[1] < 400:
        k_dn = 2.57 * pow(10, -8) * pow(fa[1], 2.4)
    elif 400 < fa[1] < 10000:
        k_dn = 1 - 1.074 * math.exp(pow(-10, -4) * pow(fa[1], 1.18))

    k_i = k_up - k_dn

    data[i].append(k_dn)
    data[i].append(k_up)
    data[i].append(k_i)

    if fa[0] <= 1000:
        d_A = 200 / pow(fa[0], 0.43) - 0.37
    else:
        d_A = 1.37 + 1000 / pow(fa[0], 0.69)
    data[i].append(d_A)


    print("  k_i =",  k_up,  "-", k_dn, "=", k_up - k_dn)

    print("Эффективный уровень ощущения формант в каждой i-ой октавной полосе частот Eфi:")
    E_fi = fa[3] - fa[4] - d_A - (Q_door[i] + Q_per)

    data[i].append(E_fi)

    print("  𝐸ф𝑖 = 𝐿сигн.𝑖 − 𝐿шума𝑖 − ∆𝐴𝑖 − 𝑄перег.𝑖: ", fa[3], fa[4], d_A, (Q_door[i] + Q_per), E_fi)

    if E_fi < 0:
        w_i = (0.78 + 5.46 * math.exp(-4.3*pow(10, -3)*pow(2.73 - abs(E_fi), 2))) / (1 + pow(10, 0.1 * abs(E_fi)))
    else:
        w_i = 1 - (0.78 + 5.46 * math.exp(-4.3*pow(10, -3)*pow(2.73 - abs(E_fi), 2))) / (1 + pow(10, 0.1 * abs(E_fi)))
    print("Коэффициенты восприятия формант в каждой i-ой октавной полосе wi: ", w_i)

    A_i = w_i * k_i

    data[i].append(w_i)
    data[i].append(A_i)

    print("Разборчивость формант в i-ой полосе частот Аi: ", A_i)

    A += A_i

print("A = ", A)

if A < 0.15:
    W = 1.54 * pow(A, 0.25) * (1 - math.exp(-11 * A))
else:
    W = 1 - math.exp((-11 * A) / (1 - 0.7 * A))
print("W = ", W*100)

print("{0:4} | {1:4} | {2:4} | {3:3} |{4:3} | {5:7} | {6:7} | {7:7} | {8:7} | {9:7} | {10:7} | {11:7}".format("f_ср", "f_ниж", "f_вер", "", "", "", "", "", "", "", "", ""))
for i in range(5):
    fa = data[i]
    print("{0:4} | {1:5} | {2:5} | {3:3} |{4:3} | {5:-7.4f} | {6:-7.4f} | {7:-7.4f} | {8:-7.4f} | {9:-7.4f} | {10:-7.4f} | {11:-7.4f}".format(fa[0], fa[1], fa[2], fa[3], fa[4], fa[5], fa[6], fa[7], fa[8], fa[9], fa[10], fa[11]))
