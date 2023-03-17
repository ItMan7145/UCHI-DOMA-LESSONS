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

# name = input("Name: ")
# type = input("Type: ")
# age = int(input("Age: "))
#
# queryInsert = QSqlQuery(connection)
# queryInsert.exec(
#     f"""
#     INSERT INTO animals(name, type, age) VALUES ('{name}','{type}', '{age}')
#     """
# )

query.exec("SELECT * FROM animals")
query.first()
print(query.value(0), query.value(1), query.value(2))
print()

# query.exec("SELECT * FROM animals")
query.last()
print(query.value(0), query.value(1), query.value(2))
print()

query.exec("SELECT * FROM animals")
while query.next():
    print(query.value(0), query.value(1), query.value(2), query.value(3))

# connection.tables()
query.finish()
# queryInsert.finish()
connection.close()
