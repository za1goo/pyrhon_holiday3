import datetime     #Импорт модуля

x = datetime.datetime.now()     #Вызов метода now из класса datetime
num_day_year = (x.strftime("%j"))   #Значение текущего дня (номер дня в году)
open_reading_file = open('holiday.txt').read().split('\n')[int(num_day_year)]   #Открытие файла с праздниками (чтение определённой строки)
print(open_reading_file)    #Вывод на экран текущей даты и праздника
if 'нет' not in open_reading_file:
    while True:
        question = input('Хотите узнать больше об этом празднике? (да/нет): ')  #Вопрос пользователю
        if question == 'нет':
            print('Программа завершена.')
            break
        elif question == 'да':
            x2 = datetime.datetime.now()    #Вызов метода now из класса datetime
            num_day_year2 = (x2.strftime("%d")) #Значение текущего дня (номер дня в месяце)
            open_reading_file2 = open('information.txt', encoding='utf-8').read().split('\n')[int(num_day_year2)] #Открытие файла с информацией о праздниках (чтение определённой строки)
            print(open_reading_file2)   #Вывод на экран информации о праздниках
            break
        else:
            print('Неккоректный ввод, попробуйте снова.')
            continue