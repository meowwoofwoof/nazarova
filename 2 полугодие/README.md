## Задачи ЕГЭ
| № | |
| ------ | ------ |
| 1 | |
| 2 | |
| 3 | |
| 4 | |
| 5 | + | 
| 6 | + |
| 7 | |
| 8 | |
| 9 | |
| 10 | |
| 11 | |
| 12 | |
| 13 | |
| 14 | |
| 15 | |
| 16 | |
| 17 | |
| 18 | |
| 19 | |
| 20 | |
| 21 | |
| 22 | |
| 23 | |
| 24 | |
| 25 | |
| 26 | |
| 27 | |


## Идеи решения задач:

**Пояснения к 5 задаче:**
  
  1. Организовать цикл перебора чисел
  
  2. Перевод числа в 2-ю СС (bin , f'{n:b}')
  
  3. Выполнение условий задачи с дописью и заменой
  
  4. Перевод в int и проверка на условие
  
  5. После вывода минимального, прерывание break
  
  Пример кода: 
  for N in range (516):
    b = f'{N:b}'
    if N % 2 == 0:
        b += '10'
    else:
        b = '1'+ b + '01'
    if int(b,2)>516:
         print(N)
         break
    

**Пояснения к 6 задаче:**
 
  1. Вспомнить команды черепашки
  
  2. Воспроизвести алгоритм задачи
 
  3. Расставить сами точки внутри контура
  
  4. Вручную посчитать точки
  (жирность точек не влияет на подсчет)

