# nazarova
Формулы в LaTeX


$$\frac{\sqrt{\frac{xb}{2}}+cos^{2}|x-b|}{\frac{x^{2}(x+1)}{b}-sin^{2}(x+a)}$$


$$C_{8}H_{18}\to C_{4}H_{10}+C_{4}H_{8}$$


$$\overline{E^{2}}_{1}=\sqrt{\frac{Fa^{^{x-1}}}{(x-1)\cdot x}} +\alpha^{\frac{1}{3}}_{1}+\beta^{\frac{2}{3}}_{2}$$


Формула по логике. Формула дистрибутивности.


$$\left(A \vee  B\right)\wedge C=\left( A\wedge C \right)\vee \left( B\wedge C \right)$$



Морзе в pyton 

abc = list('abwgdevzijklmnoprstufhcqx')
print(abc)

morze='.- -... .-- --. -.. . ...- --.. .. .--- -.- .-.. -- - --- .--. .-. ... - ..- ..-. .... -.-. --.- -..-'
m=morze.split()
print(m)
print(m[0])
input()
#перебор посимвольно текста for
#искали этот символ в алфавите по индексу и запоминали номер .index
#по этому номеру дергали элемент азбуки морзе [nomer]
text=input(введите слово...)
for i in text:
    num=abc.index(i)
    itog=itog+abcm[num]
print(itog)

