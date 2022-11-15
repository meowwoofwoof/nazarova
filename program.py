def menu1():
    print('')


def func():
    
        print('1 Кодирование информации')
        print('2 Кодирование изображения')
        print('3 Кодирование звука')
        select=int(input('Введите номер пункта -'))
    
        if select==1:
            menu2()
        elif select==2:
            menu3()
        elif select==3:
            menu4()

func()

#кодирование информации
def menu2():
    print('')


def func():
    select=0
    while select!=4:
        print('1 - i')
        print('2 - I')
        print('3 - N')
        print('4 Далее')
        select=int(input('Введите неизвестную переменную -'))
    
        if select==1:
            menu1()
        elif select==2:
            menu2()

func()def menu1():
    print('')


def func():
    select=0
    while select!=4:
        print('1 Пункт')
        print('2 Пункт')
        print('3 Пункт')
        print('4 Далее')
        select=int(input('Введите номер пункта -'))
    
        if select==1:
            menu1()
        elif select==2:
            menu2()

func()
