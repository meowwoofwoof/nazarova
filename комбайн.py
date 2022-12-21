import math
def mrz():
    s=input("введите слово через пробел заглавными латинскими буквами: ")
    str_list=s.split(sep=' ')
    d=dict(A='.-', B='-...',W='.--',G='--.',D='-..',E='',V='',Z='',I='',J='',K='',L='',M='',N='',O='---',P='.--.',R='.-.',S='...',T='',U='..--',F='..-.',H='....',C='-.-.',Q='---.-',X='-..-')
    i=len(str_list)
    for k in range(i):
        print(d[str_list[k]], end=" ")
        str_c=d[str_list[k]].split()
def distance(x,y):
    k=7
    for i in range(0,7):
        if x%10==y%10:
            k=k-1
            x=x//10
            y=y//10
    return k
def hem():
    chisla='0123456789'
    chisla_spicok=list(chisla)
    print(chisla_spicok)
    haming='0000000 0001111 0011001 0100101 0101010 0110011 0111100 1000011 1001100'
    haming_spisok=haming.split()
    print(haming_spisok)
    cod=int(input("код= "))
    min=distance(cod,int(haming_spisok[0]))
    imin=0
    for i in range(0,9):
        D=distance(cod,int(haming_spisok[i]))
        if D<min:
            min=D
            imin=i
    print(min)
    if min==0:
        print(f"код верный: символ {chisla_spicok[imin]}")
    elif min==1:
        print(f"код исправлен: символ {chisla_spicok[imin]}")
    else:
        print("неверный код")
def tot():
    p=int(input("основание (2<p<=10)"))
    n=0
    for x in range(1,p):
        for y in range(1,p):
            n=((x*y)//p)*10+x*y%p
            print(n,end=" ")
        print(" ")
def tit():
    p=int(input("число: "))
    n=int(input("сс: "))
    k=1
    d=0
    while(n!=0):
        d+=n%10*k
        k=k*p
        n=n/10
    print(d)
def tut():
    n = int(input("число: "))
    c=int(input("в сс:"))
    b = ''
    while n > 0:
        b = str(n % c) + b
        n = n // c
    print(b)
def menu():
    print(" ")
    print("1 - морзянка")
    print("2 - код Хэмминга")
    print("3 - перевод из n-ой в 10-ую")
    print("4 - таблица умножения n-ой")
    print("5 - перевод из десятичной в n-ую")
    m=int(input("Какую задачу выполняем? (чтобы вернуться обратно, тыкай нолик:)):"))
    if(m==1):
        mrz()
    elif(m==2):
        hem()
    elif(m==3):
        tot()
    elif(m==4):
        tit()
    elif(m==5):
        tut()
    else:
        print("еще разок")
while 1 >0:
    menu()
