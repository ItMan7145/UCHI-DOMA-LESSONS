def get_address():
    address = input()

    if '@' in address and '.' in address:
        print('Верно')
    elif '@' not in address and '.' not in address:
        print('Отсутствует @ и .')
    elif '@' not in address:
        print('Отсутствует @')
    elif '.' not in address:
        print('Отсутствует .')


get_address()
