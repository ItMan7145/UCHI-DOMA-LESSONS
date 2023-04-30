from datetime import datetime

from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, length

# images_folder = os.path.join('static', 'images')
# , static_url_path='/static'
app = Flask(__name__)

app.config[
    'SECRET_KEY'] = '\x89\xb3I\xf9?v4+R\xb1_l\xac\xdem\x9f\xd5\xc9sY<+V\x7fK\xcb\x97\xcd\x1c\xfeiE\xbc)E\xc4\xc1\x9c\
    xa7\xea\xd7Dj\xb4\x9cX{8\xcb\xa8%\x04\to\xab|\x18\xf2\xc6d\x0b&\xd6\xfc6\xe4\x16d\x9b\x90\x8bo\x16\xe6\xdc\xb7\xa5\
    xcaAa(\xf8\xcf\x13IOv$\x97\xe5\xf3=\xaa0m\xb0\xb6\xbc\x8a\x82\xc7\xedH\xfd(\xf2qk\xbb\xa6\x90\x8f\\\xc8\x1b\xbai\
    xf5\xf5\xd9\x14\xb3\xcdzC\xf7"\xd7v\x85\xa2o\x1f>\xbd:\xa7\xad\x0e\x80a\xd8\xd8\xd9\xd0\x07\x1e\x05`\xec\xbe\xa2g4N\
    x8a\xba oF\x85r\r$\x16\xf9\xc2\xf92\xd0\x0b\\b\nSD\x00U\xab\xd1I\x9c\x89\xa2\x93\\\xcaR&\xac\x9e\xe0\x83\xd6l\xabpd\
    x01K\xda\xe4V\x8b\xf6Y-9-\xf2\x92g\xe4ULJ\xbe/\'#F\x04Y\x8b\xa4|\x80\xcbS\x9cl3`\x9f\xf20VO\x98N'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask-site-db.sqlite3'
# app.config['UPLOAD_FOLDER'] = images_folder

db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    news = db.relationship('News', back_populates='category')


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    category = db.relationship('Category', back_populates='news')


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


news = [{'title': 'О проекте ',
         'text': 'Данный проект создан по инициативе Министерства Просвещения России. На реализацию сайта были '
                 'выделены денежные средства в размере 2 180 450 000 рубелей  '},

        {'title': 'Кратко: ежедневный брифинг Евгения Канашынкова',
         'text': 'Ежедневный брифинг минизверства обороны Российской Федерации. Хотелось бы отметить, что наша '
                 'молниеносная спецоперация, которой сегодня исполняется 424 дня, находится можно сказать, в самом разгаре! '
                 'Так, за последние сутки разгорелось 12 наших танков. Перейдем к главным событиям, о которых говорить пока '
                 'разрешили. На днях неподалеку от Украины с нашего самолета СУ-34 произошел "нештатный сход авиационного '
                 'боеприпаса". Как стало известно боеприпас нештатно сходил прогуляться в центр Белгорода. В результате данной '
                 'прогулки произошел небольшой "шлепок" с  дальнейшим "хлопком" на перекрестке улиц Губкина и Ватутина. '
                 'По предварительной информации, ни одна Ватутина и Губкина на перекрестке не пострадали. Но при этом в '
                 'результате данного шлепо-хлопка один из автомобилей, который находился неподалеку, '
                 'неожиданно стал находиться подалеку.'},

        {'title': '30.02.23 Солофьев: "Освобождение Окраины будет завершено к началу апреля 2023..."',
         'text': 'Укронацисты, сдавайтесь! Загнивающий Запад больше не будет спонсировать вашу нацистскую власть! '
                 'Экономика Америки придет в упадок! Продавайте скорее доллары и покупайте самую стабильную '
                 'валюту - рубли (или теньге)'},

        {'title': 'Росстат: Путина поддерживают 118% граждан',
         'text': 'Росстат: рейтинги бьют все рекорды! Путина поддерживают 118% граждан!'},

        {'title': 'Внимание! 2 апреля в Санкт-Петербурге взорвался кафе с ...',
         'text': 'Вдалден Тарарский был очень раздосадован неправильным приготовлением капучино, после он осуществил '
                 'самохлопок с неконтролируемым выбросом тепловой энергии, вследствие произошел отрицательный рост '
                 'населения России в количестве 1 человека'},

        {'title': 'Весеннее контр наступление Окраины обозначено на...',
         'text': 'Разведка подтвердила информацию о готовящемся наступлении Окраины. Оно произойдет 20 апреля '
                 '2023 года в 23 часа 78 минут по МСК.'},

        {'title': 'Скорее закупайте гречку и доллары! Скоро наступит...',
         'text': 'Скоро наступит весеннее контрнаступление с последующим контротступлением, выполняя тактические '
                 'перегруппировки с переподвыперегрупировкой '},

        {'title': 'Итоги выборов. За партию вЕдРо проголосовало 103% избирателей',
         'text': 'Итоги выборов. За партию вЕдРо проголосовало 103%'},

        {'title': 'Раскрыт новый рецепт селедки с молоком. Я всего-лишь добавил...',
         'text': 'Раскрыт новый рецепт селедки с молоком. Я всего-лишь добавил одну ложку активированного угля'},

        {'title': 'Вы выиграли в анонимной лотерее 1 000 000 рублей! '
                  '(Для получения необходимо заплатить комиссию 1000 руб)',
         'text': '28.04.2023 была проведена анонимная лотерея. победителем '
                 'были объявлены именно вы. Для получения выигрыша заплатите комиссию за перевод - 1000 рублей'},

        {'title': 'Важно! Найдено средство лечения от рака, нужно принимать обычный советский...',
         'text': 'Важно! Найдено средство лечения от рака, надо принимать обычный советский крем-бальзам Звездочка'},
        ]


@app.route('/')
def index():
    news_list = News.query.all()
    return render_template('index.html', news=news_list)


@app.route('/news_detail/<int:news_id>')
def news_detail(news_id):
    news = News.query.get(news_id)
    return render_template('news_detail.html', news=news)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/create_news', methods=['POST', 'GET'])
def create_news():
    form = NewsForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        db.session.add(news)
        db.session.commit()
        # news.append({'title': title, 'text': text})
        return redirect(url_for('index'))
    return render_template('create_news.html', form=form)


@app.route('/create_category', methods=['POST', 'GET'])
def create_category():
    form = CategoriesForm()
    if form.validate_on_submit():
        category = Category()
        category.title = form.title.data
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_category.html', form=form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=8000)
