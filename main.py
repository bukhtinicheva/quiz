import sqlite3
import random

def format_osn(stroka):
    a = []
    for i in range(len(stroka)):
        a.append(str(stroka[i])[1:-2])
    a = str(a)
    a = a.replace("[", '')
    a = a.replace("]", '')
    a = a.replace("'", '')
    a = a.replace(",", '')
    a = list(a)
    return ''.join(a[1:-1])

def format_cor(stroka):
    a = []
    for i in range(len(stroka)):
        a.append(str(stroka[i])[1:-2])
    a = str(a)
    a = a.replace("[", '')
    a = a.replace("]", '')
    a = a.replace("'", '')
    a = a[1:-1]
    a = a.split(", ")
    return a

def format_ans(stroka):
    a = []
    for i in range(len(stroka)):
        a.append(str(stroka[i])[2:-2])
    a = str(a)
    a = a.replace("[", "")
    a = a.replace("]", "")
    a = a.replace("'", "")
    a = a.replace(",", "")
    a = a[1:]
    a = list(a)
    for i in range(len(a)):
        if a[i].isupper() or a[i].isdigit():
            a[i-1] = ', '
    return "".join(a[:-1])

flag = True
level = 1
while flag and level <= 5:
    print(f'Уровень {level}')
    a = []
    connection = sqlite3.connect("quizz.db")
    cursor = connection.cursor()
    count_quest = cursor.execute(f"""SELECT id FROM level_{level}""").fetchall()
    lenght = [i for i in range(1, len(count_quest) + 1)]
    number_s = random.sample(lenght, 4)
    count = 0
    fl = True
    while fl and count < 2:
        count += 1
        question = format_osn(cursor.execute(f"""SELECT question FROM level_{level} WHERE id = {number_s[count - 1]}""").fetchall())
        ansers = format_ans(cursor.execute(f"""SELECT ans_1, ans_2, ans_3, ans_4 FROM level_{level} WHERE id = {number_s[count - 1]}""").fetchall())
        print(f'Внимание, вопрос: {question}')
        print(f'Варианты ответа: {ansers}')
        correct = format_cor(cursor.execute(f"""SELECT correct_ans FROM level_{level} WHERE id = {number_s[count - 1]}""").fetchall())
        anser = input()
        if anser in correct:
            print('Правильный ответ\n')
        else:
            print('Неправильный ответ. Вы проиграли')
            fl = False
    if fl == False:
        flag = False
    if flag:
        if count == 2:
            print(f'Поздравляю, вы прошли уровень {level}!')
            print('-----------------------------------------')
            count = 0
            if level == 5:
                print('Поздравляю! Вы прошли викторину!')
            level += 1