import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
#
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
#
# plt.subplot(3, 2, 1)
# plt.plot(x1, y1, '-')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykresy funkcji sin(x)')
#
# plt.show()
#
# plt.subplot(324)
# plt.plot(x2, y2, 'r-')
# plt.ylabel('cos(x)')
# plt.xlabel('x')
# plt.title("Wykres funkcji cos(x)")
#
# plt.subplot(3, 2, 5)
# plt.plot(x2, y2, 'r-')
# plt.ylabel('cos(x)')
# plt.xlabel('x')
# plt.title("Wykres funkcji cos(x)")
#
# plt.show()
#
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('wartości a')
# plt.ylabel('wartości b')
# plt.show()
#
# etykiety = ['Kobiety', 'Mężczyźni']
# wartosci = [345, 435]
#
# rozmiar = plt.figure(figsize=(8,10))
# plt.bar(etykiety, wartosci, figure=rozmiar)
#
# plt.xticks(rotation=45)
# plt.xlabel('Płeć')
# plt.ylabel('Ilość narodzin')
#
# plt.show()

# x = np.random.randn(10000)
#
# plt.hist(x, bins=25, facecolor='g', alpha=0.75, density=True)
#
# plt.xlabel('Wartości')
# plt.ylabel('Prawdopodobieństwa')
# plt.title('Histogram')
#
# plt.grid()
# plt.show()

# zawodnicy = ['Messi', 'Suares', 'Dembele', 'Coutinho']
# bramki = [48, 25, 13, 11]
#
# wedegs, texts, autotexts = plt.pie(bramki, labels=zawodnicy,
#                                    autopct=lambda pct:
#                                    "{:.1f}%".format(pct), textprops=dict(color='black'))
# plt.setp(autotexts, size=14)
# plt.title("Wykres kołowy z procentowym udziałem strzelonych goli")
# plt.legend(title='Zawodnicy')
# plt.show()
# =================
# pr.domowa
# =================
# zad1
# x = np.arange(20,41,1)
# a = 1/x
# plt.plot(x, a)
# plt.xlabel('x')
# plt.ylabel('1/x')
# plt.margins(0)
# plt.ylim(ymin=0.02)
# plt.title('Wykresy funkcji f(x) dla x[20,40]')
# plt.show()
# zad2
x = np.arange(20,41,1)
a = 1/x
plt.plot(x,a, "bo--")
plt.title("Wykres funckji f(x) dla x[20,40]")
plt.xlabel("x")
plt.ylabel("1/x")
plt.margins(0)
plt.ylim(ymin=0.02)
plt.show()
