from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, length

class NewsForm(FlaskForm):
    title = StringField('Название', validators=[
        DataRequired(message='Да ты йёнутый! Иди лечись пока не поздно! Заполни поле, тебе же сказали!'),
        length(max=255, min=3, message='Введи заголовок длиной от 3 до 255 символов!')])
    text = TextAreaField(
        'Текст', validators=[DataRequired(message='Не суди по себе! Поле не должно быть пустым как твоя голова!')])
    submit = SubmitField('Вызвать ОМОН')


class CategoriesForm(FlaskForm):
    title = StringField('Название катерогии', validators=[
        DataRequired(message='Да ты йёнутый! Иди лечись пока не поздно! Заполни поле, тебе же сказали!'),
        length(max=255, min=3, message='Введи заголовок длиной от 3 до 255 символов!')])
    submit = SubmitField('Придумать категорию лжи')


class SignInForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[
        DataRequired(message='Да ты йёнутый! Иди лечись пока не поздно! Заполни поле, тебе же сказали!'),
        length(max=255, min=3, message='Введи имя пользователя длиной от 3 до 255 символов!')])
    password = PasswordField('Пароль', validators=[
        DataRequired(message='Да ты йёнутый! Иди лечись пока не поздно! Заполни поле, тебе же сказали!'),
        length(max=255, min=3, message='Введи пароль длиной от 3 до 255 символов!')
    ])
    submit = SubmitField('Вызвать ОМОН')


class SignUpForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[
        DataRequired(message='Да ты йёнутый! Иди лечись пока не поздно! Заполни поле, тебе же сказали!'),
        length(max=255, min=3, message='Введи имя пользователя длиной от 3 до 255 символов!')])
    email = EmailField('Почта')
    password = PasswordField('Придумайте пароль', validators=[
        DataRequired(message='Да ты йёнутый! Иди лечись пока не поздно! Заполни поле, тебе же сказали!'),
        length(max=255, min=3, message='Введи пароль длиной от 3 до 255 символов!')
    ])
    submit = SubmitField('Вызвать ОМОН')


