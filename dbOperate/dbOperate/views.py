from django.shortcuts import render
from django.db import connection


def index(request):
    cursor = connection.cursor()
    # cursor.execute("INSERT INTO `db1`.`book`( `book`, `author`) VALUES ('1', '1');")
    cursor.execute("SELECT * FROM book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request, 'index.html')
