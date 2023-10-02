# import pymysql
# from lesson_6.configs.config_sql_connection import host, user, password, db_name, port, db_name2
# from lesson_6.configs.config import paths
#
#
#
# try:
#     connection1 = pymysql.connect(
#         host=host,
#         port=port,
#         user=user,
#         password=password,
#         database=db_name,
#     )
#     print("Succsesfully connected...")
#     cursor = connection1.cursor()
#
#     try:
#         sql_query = "SELECT * FROM users"
#         cursor.execute(sql_query)
#         rows = cursor.fetchall()
#     finally:
#         connection1.close()
# except Exception as e:
#     print("Connection refused....")
#     print(e)
#
#
#
#
# try:
#     connection2 = pymysql.connect(
#         host=host,
#         port=port,
#         user=user,
#         password=password,
#         database=db_name2,
#     )
#     print("Succsesfully connected second db...")
#     cursor2 = connection2.cursor()
#
#     try:
#        # for row in rows:
#        #     with open("../scripts/users_table/add_data.sql") as sql_add_data:
#        #         add_data = f"{sql_add_data.read()} {str(row[0:5])}"
#        #     cursor2.execute(add_data)
#
#
#        cursor2.execute("select id from users order by id asc")
#        ids = cursor2.fetchall()
#        ind = 0
#
#        for row in rows:
#             for path in paths:
#                 path_link, data_indexes = path
#                 data = list(row[data_indexes[0]:data_indexes[1]])
#                 data.append(ids[ind][0])
#                 data = tuple(data)
#                 with open(path_link, "r") as sql_code:
#                     query = f"{sql_code.read()} {data}"
#
#                 cursor2.execute(query)
#             ind += 1
#
#
#
#        connection2.commit()
#
#
#
#     finally:
#         connection2.close()
# except Exception as e:
#     print("Connection refused second db....")
#     print(e)
