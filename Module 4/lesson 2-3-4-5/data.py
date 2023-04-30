import sqlite3

db = sqlite3.connect('flask-site-db.db')
sql = db.cursor()
sql.execute('INSERT INTO news(title, text, create_date) VALUES (?, ?, ?)', ('title', 'text', 'datetime.utcnow'))
db.commit()
