from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, FileField
from flask_wtf.file import FileAllowed, FileRequired
from wtforms.validators import DataRequired, length, Optional


class ReviewForm(FlaskForm):
    name = StringField('Имя', validators=[
        DataRequired(message=' Заполни поле, тебе же сказали!'),
        length(max=255, min=3, message='Введи заголовок длиной от 3 до 255 символов!')])
    text = TextAreaField(
        'Текст', validators=[DataRequired(message='Не суди по себе! ')])
    score = SelectField('Рейтинг фильма', choices=[(i, i) for i in range(1, 11)], validators=[])
    submit = SubmitField('Добавить свой паршивый никому не нужный отзыв. Эксперт ты диванный хренов')


class MovieForm(FlaskForm):
    title = StringField('Имя', validators=[
        DataRequired(message='Да ты йёнутый! Иди лечись пока не поздно! Заполни поле, тебе же сказали!'),
        length(max=255, min=3, message='Введи заголовок длиной от 3 до 255 символов!')])
    description = TextAreaField(
        'Текст', validators=[DataRequired(message='Не суди по себе! Поле не должно быть пустым как твоя голова!')])
    image = FileField('Изображение', validators=[
        FileRequired(message='Поле не должно быть пустым как твоя голова!'),
        FileAllowed(['img', 'jpeg', 'png', 'jpg'], message='Да ты йёнутый! Иди лечись пока не поздно! Формат не тот')
    ])
    submit = SubmitField('Добавить свой паршивый никому не нужный фильм, мамкин режиссер')
