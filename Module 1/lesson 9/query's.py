from main import *

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
