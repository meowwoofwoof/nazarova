ls = [
    ("мяу?", "да"),
    ("Павел Николаевич самый лучший учитель?", "да"),
    ("?", "нет"),
]
 
for q, a in ls:
    print(q, '[да/нет]')
    answer = input().strip().lower()
    if answer == a:
        print("правильный ответ")
    else:
        print("неправильный ответ")
