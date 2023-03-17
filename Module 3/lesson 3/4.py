user_name = input('Введите ваше имя:')
while True:
    try:
        print('Выберите действие:\n'
              '1.Посмотреть текущий текст чата\n'
              '2.Отправить сообщение.')
        action = int(input(': '))

        if action == 1:
            try:
                with open('C:/Users/Валера/PycharmProjects/UDPro/module3/3/Chat.txt', 'r') as chat:
                    for i_line in chat:
                        print(i_line)
            except FileNotFoundError:
                print('Файл не найдет.')
        elif action == 2:
            try:
                with open('C:/Users/Валера/PycharmProjects/UDPro/module3/3/Chat.txt', 'a') as chat:
                    text = input('Введите сообщение: ')

                    chat.write('{name}: {text}\n'.format(name=user_name, text=text))
            except FileNotFoundError:
                print('Фаил не найдет.')
        else:
            print('Ошибка ввода, попробуйте еще раз!')
    except Exception as ex:
        print(ex)

# str.split()
# import da
