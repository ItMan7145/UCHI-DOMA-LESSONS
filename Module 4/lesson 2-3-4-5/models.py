from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# images_folder = os.path.join('static', 'images')
# , static_url_path='/static'
app = Flask(__name__)
app.config['SECRET_KEY'] = '\x89\xb3I\xf9?v4+R\xb1_l\xac\xdem\x9f\xd5\xc9sY<+V\x7fK\xcb\x97\xcd\x1c\xfeiE\xbc)E\xc4\xc1\x9c\
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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(329), nullable=True)
    reg_date = db.Column(db.DateTime, default=datetime.utcnow().strftime('%d.%m.%Y %H:%M'))
    admin = db.Column(db.Boolean, nullable=False, default=False)
