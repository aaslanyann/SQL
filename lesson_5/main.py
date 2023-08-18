import pymysql
from config import host, user, password, db_name, port


try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db_name,
    )
    print("Succsesfully connected...")
    cursor = connection.cursor()

    try:
      with open("users_finances_table/users_finances.txt", "r") as txt:
          sql_query = txt.read().replace("\n", "")

      cursor.execute(sql_query)

      with open("users_finances_table/add_data.txt", "r") as txt:
          sql_query = txt.read().replace("\n", "")

      cursor.execute(sql_query)
      connection.commit()


    finally:
        connection.close()
except Exception as e:
    print("Connection refused....")
    print(e)


