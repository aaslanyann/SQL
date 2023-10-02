import pymysql
from lesson_8.configs.config_sql_connection import host, user, password, db_name, port
from tables.cars import cars_controller
from tables.users import users_controller
from tables.users_details import details_controller
from tables.users_finances import finances_controller
from tables.users_mobiles import mobiles_controller



try:
  chosen_table = input("Choose a table... (cars, users, users_details, users_mobiles, users_finances) ").lower().strip()
  connection = pymysql.connect(
      host=host,
      port=port,
      user=user,
      password=password,
      database=db_name,
  )
  print("Succsesfully connected...")
  cursor = connection.cursor()

  sql_query_users = "SELECT * FROM users"
  cursor.execute(sql_query_users)
  users_data = cursor.fetchall()



  if chosen_table == 'users':
    callback_answer = users_controller.user_controller(users_data)
  elif chosen_table == 'cars':
    cursor.execute('select * from cars')
    cars_data = cursor.fetchall()
    callback_answer = cars_controller.car_controller(users_data, cars_data)
  elif chosen_table == 'users_details':
    cursor.execute('select * from users_details')
    users_details = cursor.fetchall()
    callback_answer = details_controller.detail_controller(users_data, users_details)
  elif chosen_table == 'users_finances':
    cursor.execute('select * from users_finances')
    finance_data = cursor.fetchall()
    callback_answer = finances_controller.finance_controller(users_data, finance_data)
  elif chosen_table == 'users_mobiles':
    cursor.execute('select * from users_mobiles')
    mobile_data = cursor.fetchall()
    callback_answer = mobiles_controller.mobile_controller(users_data, mobile_data)
  else:
    print('There is no such table')

  cursor.execute(callback_answer)

  print('Command successfully...')

  connection.commit()

except Exception as e:
  print(e)
finally:
  connection.close()