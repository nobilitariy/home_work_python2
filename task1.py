'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток,
которые нужно перевернуть, чтобы все монетки были повернуты вверх одной
и той же стороной. Выведите минимальное количество монет,
которые нужно перевернуть'''

mon = int(input('Введите колличество монет '))
orel = 0
resh = 0
for i in range(mon):
    storona = int(input('Сторона монетки(1 - орел, 0  - решка) - '))
    if storona == 1:
        orel += 1
    else:
        resh += 1
if orel != 0 and resh != 0 and orel != resh:
    if orel > resh:
        print(f'Быстрее перевернуть {resh} монет(ы) орлом вверх')
    else:
        print(f'Быстрее перевернуть {orel} монет(ы) решкой вверх')
elif resh == 0 or orel == 0:
    print('Ничего переворачивать не нужно')
else:
    print('Переворачивай что хочешь')