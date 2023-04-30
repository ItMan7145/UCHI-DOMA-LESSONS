import sqlite3
from datetime import datetime

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, length

try:
    db = sqlite3.connect('flask-site-db.db', check_same_thread=False)
    sql = db.cursor()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'


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


@app.route('/')
def index():
    sql.execute('SELECT * FROM news')
    news_list1 = sql.fetchall()
    # news_list2 = [{
    #     'id': 0,
    #     'title': 'None',
    #     'text': 'None',
    #     'create_date': 'None'
    # }]
    # print(news_list1)
    # for el in news_list1:
    #     news_list2.append({'id': el[0], 'title': el[1], 'text': el[2], 'create_date': el[3]})
    # print(news_list2)
    return render_template('index.html', news=news_list1)


@app.route('/news_detail/<int:news_id>')
def news_detail(news_id):
    sql.execute(f'SELECT * FROM news WHERE id={news_id}')
    news = sql.fetchone()
    return render_template('news_detail.html', news=news)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create_news', methods=['POST', 'GET'])
def create_news():
    form = NewsForm()
    if form.validate_on_submit():
        title = str(form.title.data)
        text = str(form.text.data)
        try:
            sql.execute('INSERT INTO news(title, text, create_date) VALUES (?, ?, ?)',
                        (title, text, str(datetime.utcnow().strftime('%d.%m.%Y %H:%M'))))
            db.commit()

        except sqlite3.Error as error:
            print('[ERROR]', error)
        return redirect(url_for('index'))
    return render_template('create_news.html', form=form)


@app.route('/create_category', methods=['POST', 'GET'])
def create_category():
    form = CategoriesForm()
    if form.validate_on_submit():
        title = form.title.data

        return redirect(url_for('index'))
    return render_template('create_category.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
    # pass
