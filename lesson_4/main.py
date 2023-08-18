import pymysql
from config import host, user, password, db_name, port


try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Succsesfully connected...")

    try:

        with connection.cursor() as cursor:
            select_all_rows = "SELECT * FROM `users`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()

            for row in rows:
                print(row)
            print("#" * 20)

    finally:
        connection.close()
except Exception as e:
    print("Connection refused....")
    print(e)


