import sqlite3
from datetime import datetime

from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, length

try:
    db = sqlite3.connect('flask-site-db.db', check_same_thread=False)
    sql = db.cursor()
except sqlite3.Error as error:
    print('[ERROR: CONNECT DATABASE]', error)

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


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/news_detail/<int:news_id>', methods=['POST', 'GET'])
def news_detail(news_id):
    sql.execute(f'SELECT * FROM news WHERE id={news_id}')
    news = sql.fetchone()
    return render_template('news_detail.html', news=news)


@app.route('/news_detail/<int:news_id>/delete')
def news_delete_confirm(news_id):
    try:
        sql.execute(f'DELETE FROM news WHERE id={news_id}')
        db.commit()
        return redirect(url_for('index'))
    except sqlite3.Error as error:
        print('[ERROR: DELETE NEWS]', error)


# @app.route('/news_detail/<int:news_id>/delete')
# def news_delete(news_id):
#     # return render_template('news_delete.html', news_id=news_id)
#     sql.execute(f'SELECT * FROM news WHERE id={news_id}')
#     news = sql.fetchone()
#     return render_template('news_detail.html', news=news)


# @app.route('/news_detail/<int:news_id>/delete/confirm')
# def news_delete_confirm(news_id):
#     try:
#         sql.execute(f'DELETE FROM news WHERE id={news_id}')
#         db.commit()
#         return redirect(url_for('index'))
#     except sqlite3.Error as error:
#         print('[ERROR]', error)

@app.route('/news_detail/<int:news_id>/edit', methods=['POST', 'GET'])
def news_edit(news_id):
    form = NewsForm()
    if form.validate_on_submit():
        title = str(form.title.data)
        text = str(form.text.data)
        create_date = str(datetime.utcnow().strftime('%d.%m.%Y %H:%M'))
        try:
            sql.execute(f'UPDATE news SET title={title}, text={text}, create_date={create_date} WHERE id={news_id}')
            db.commit()
        except sqlite3.Error as error:
            print('[ERROR: NEWS EDIT]', error)
        return redirect(url_for('index'))
    return render_template('create_news.html', form=form)


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
            print('[ERROR: CREATE NEWS]', error)
        return redirect(url_for('index'))
    return render_template('create_news.html', form=form)


@app.route('/create_category', methods=['POST', 'GET'])
def create_category():
    form = CategoriesForm()
    if form.validate_on_submit():
        title = form.title.data

        return redirect(url_for('index'))
    return render_template('create_category.html', form=form)


@app.route('/sign', methods=['POST', 'GET'])
def sign():
    form = SignInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        reg_date = str(datetime.utcnow().strftime('%d.%m.%Y %H:%M'))
        try:
            sql.execute(f'SELECT * FROM users WHERE username={username}')
            if sql.fetchone():
                print('Вход в аккаунт')
            else:
                sql.execute('INSERT INTO users(username, password, reg_date) VALUES (?, ?, ?)',
                            (username, password, reg_date))
                db.commit()
                return redirect(url_for('index'))
        except sqlite3.Error as error:
            print('[ERROR: SIGN]', error)
    return render_template('sign.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
    # pass
