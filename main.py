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
# x = np.arange(20,41,1)
# a = 1/x
# plt.plot(x,a, "bo--")
# plt.title("Wykres funckji f(x) dla x[20,40]")
# plt.xlabel("x")
# plt.ylabel("1/x")
# plt.margins(0)
# plt.ylim(ymin=0.02)
# plt.show()
# zad3
# x = np.arange(0, 45, .1)
# plt.plot(x, np.sin(x), 'b', label='sin(x)')
# plt.plot(x, np.cos(x), 'r', label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x) cos(x)')
# plt.legend(loc='upper right')
# plt.title('Wykres sin(x), cos(x)')
# plt.show()
# zad4
# x = np.arange(0, 45, .1)
# plt.plot(x, np.sin(x)+2, label='sin(x)')
# plt.plot(x, np.sin(x)*(-1), label='sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x), sin(x)')
# plt.legend(loc='center left')
# plt.show()
# zad5
# df = pd.read_csv('iris.data', sep=',', decimal='.', header=None)
# print(df)
# # przygotowanie wektora kolorow
# colors = np.random.randint(0, 50, len(df.index))
# #przygotowanie wektora z rozmiarami 'kropek'
# scale = [np.abs(df[0].iloc[x] - df[1].iloc[x]) for x in range(len(df.index))]
# # można te wielkości troszeczke 'podrasować'
# # scale = [np.abs(df[0],iloc[x] - df[1]/iloc[x]) * 5 for in range(len(df.index))]
#
# plt.scatter(df[0], df[1], c=colors, s=scale)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()
# zad6
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)

plt.subplot(1, 3, 1)
grouped = df.groupby('Plec').agg({'Liczba': ['sum']}).unstack()

grouped.plot.bar(color=['r','g'])
plt.xlabel('Płeć')

# wykres 2
plt.subplot(1, 3, 2)
x = df['Rok'].unique()
kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
print(mezczyzni)
plt.plot(x, kobiety, label="Kobiety")
plt.plot(x, mezczyzni, label="Mężczyźni")
plt.ylabel('Liczba narodzonych dzieci')

# wykres 3
plt.subplot(1, 3, 3)
x = df['Rok'].unique()
# bez funkcji falteen matplotlib wyrzuca wyjątek, który informuje nas, że nie można
# przekazywać parametru jako tablicy wielowymiarowej a w takiej postaci w tym przypadku
# zwracany jest wektor y, korzystamy wiec z flatten() poznan przy okazji omawiania biblioteki numpy
y. df.groupby('Rok').agg({'Liczba':['sum']}).values.flatten()

plt.bat(x, y)
# # Wyświetlamy cały wykres
plt.show()
#zad 7
df = pd.read_csv('zamowienia.csv', sep=';')
policzone = df.groupby('Sprzedawca')['Utarg'].sum()
# explode
explode = [0.0 for n in range(len(policzone.index))]
# określamy które kawałki i o ile wysunąć, tu losujemy jeden
explode[np.random.randint(0, len(policzone.index))] = 0.2
policzone.plot.pie(subplots=True, autopct='%.2f %%', fontsize=8, explode=explode, shadows=True)
plt.title("Procentowy udział zamówień sprzedawców")
plt.show()


