import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSql

connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName("database.sqlite")
print(connection.connectionName())
print(connection.databaseName())

connection.open()

if connection.isOpen():
    print("Connection succeeded")
else:
    print(connection.lastError().databaseText())
    sys.exit()

query = QSqlQuery(connection)
query.exec(
    """
    CREATE TABLE IF NOT EXISTS animals (
        id INTEGER PRIMARY KEY UNIQUE NOT NULL,
        name VARCHAR(255),
        type VARCHAR(255),
        age INTEGER
    )
    """
)
