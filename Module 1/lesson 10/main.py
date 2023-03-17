import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

connection = QSqlDatabase.addDatabase("QSQLITE")
connection.setDatabaseName("contacts.sqlite")

# print(connection.connectionName())
# print(connection.databaseName())
connection.open()
# if connection.open():
#     print("Connection succeeded")
# else:
#     print(connection.lastError().databaseText())
#     sys.exit(1)

# query = QSqlQuery(connection)
# query.exec("SELECT name, MAX(salary) FROM users WHERE job_id = 2")

# query.exec(
#     """
#     SELECT * FROM users WHERE email IS NOT NULL
#     """
# )
# while query.next():
#     print(query.value(0))
#
#
# query.exec(
#     """
#     SELECT * FROM users WHERE job_id != 1
#     """
# )
# while query.next():
#     print(query.value(0))
#
#
# query.exec(
#     """
#     SELECT name, salary FROM users WHERE salary > 5000 AND salary < 10000
#     """
# )
# while query.next():
#     print(query.value(0), query.value(1))
#
#
# query.exec(
#     """
#     SELECT name FROM users WHERE name LIKE "% Adamson"
#     """
# )
# while query.next():
#     print(query.value(0))

# count = query.record().count()
# print(count)

# for i in range(count):
#     print(query.record().fieldName(i), end="\t")
# print()
# while query.next():
#     for i in range(count):
#         print(query.value(i), end='\t')
#     print()


query = QSqlQuery(connection)
# query.exec("INSERT INTO users (name, job_id, salary) VALUES ('Arslan', 5, 100000000)")

query.exec("INSERT INTO jobs (name) VALUES ('Мыльщик полов')")

query.exec("UPDATE users SET job_id = 6, salary = 1000 WHERE name = 'Arslan' ")
