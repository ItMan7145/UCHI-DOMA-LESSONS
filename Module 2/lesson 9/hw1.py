class WrongCharacterError(Exception):
    def __init__(self):
        print('username может содержать только буквы и цифры')


class FirstCharacterError(Exception):
    def __init__(self):
        print('username не может начинаться с цифры')


username = input()

try:
    if not username.isalnum():
        raise WrongCharacterError
    if username[1].isdigit():
        raise FirstCharacterError

except WrongCharacterError:
    pass
except FirstCharacterError:
    pass
else:
    print('OK')
