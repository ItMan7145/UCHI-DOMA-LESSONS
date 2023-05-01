from flask import render_template, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from forms import NewsForm, CategoriesForm, RegisterForm
from models import *


@app.route('/')
def index():
    news_list = News.query.all()
    return render_template('index.html', news=news_list)


@app.route('/about')
def about():
    return render_template('about.html')


@login_required
@app.route('/news/<int:news_id>')
def news_detail(news_id):
    news = News.query.get(news_id)
    return render_template('news_detail.html', news=news)


@login_required
@app.route('/create_news', methods=['POST', 'GET'])
def create_news():
    form = NewsForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        db.session.add(news)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_news.html', form=form)


@login_required
@app.route('/news/<int:news_id>/edit')
def news_edit(news_id):
    form = NewsForm()
    if form.validate_on_submit():
        news = News()
        news.title = form.title.data
        news.text = form.text.data
        # db.session.
        # db.session.add(news)
        # db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_news.html', form=form)


@login_required
@app.route('/news/<int:news_id>/delete')
def news_delete(news_id):
    news = News.query.get(news_id)
    db.session.delete(news)


@login_required
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


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        hash_password = generate_password_hash(password)
        user = User(username=username, password=hash_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            # flash('Login or password is not correct')
            pass

    return render_template('login.html')


@login_required
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('/'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=7000)
