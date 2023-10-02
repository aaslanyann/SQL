import pymysql
from configs.config_sql_connection import host, user, password, db_name, port
from sql_querys import sql_request_data, sql_add_info_transactions, sql_card_amount_change


try:
  connection = pymysql.connect(
      host=host,
      port=port,
      user=user,
      password=password,
      database=db_name,
  )
  cursor = connection.cursor()
  cursor.execute(sql_request_data)
  dates = cursor.fetchall()

  for data in dates:
      print(data)

  from_user = int(input("From which ID to make the transfer? "))
  to_user = int(input("Which ID should I transfer to? "))
  much_money = input("How much money do you transfer? ")

  for data in dates:
   if int(data[0]) == from_user:
       from_user_data = data
   elif int(data[0]) == to_user:
       to_user_data = data



  if int(from_user_data[4]) < int(much_money):
    cursor.execute(sql_add_info_transactions + f"({much_money}, {from_user}, {to_user}, 'fail')")
    connection.commit()
    raise Exception("Failed: There is not that much money on this credit card ")

  cursor.execute(sql_card_amount_change.format(
      f"{int(from_user_data[4]) - int(much_money)}",
      from_user)
  )

  cursor.execute(sql_card_amount_change.format(
      f"{int(to_user_data[4]) + int(much_money)}",
      to_user)
  )



  cursor.execute(sql_add_info_transactions + f"({much_money}, {from_user}, {to_user}, 'success')")


  print('Command successfully...')

  connection.commit()

except Exception as e:
  print(e)
finally:
  connection.close()