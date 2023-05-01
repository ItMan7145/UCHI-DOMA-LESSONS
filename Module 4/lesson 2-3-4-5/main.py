from flask import render_template, redirect, url_for

from forms import NewsForm, CategoriesForm
from models import *


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
