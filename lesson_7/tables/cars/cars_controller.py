import math

def car_controller(users_data, cars_data):
  action = input('What action do you want to take? (create, update, delete, list) ').lower().strip()

  if action == 'create':
    callback_value = create_car(users_data)
  elif action == 'update':
    callback_value = update_car(cars_data)
  elif action == 'delete':
    callback_value = delete_car(cars_data)
  elif action == 'list':
    callback_value = list_car(cars_data)
  else:
    raise Exception('ERROR: No such action')

  return callback_value

def create_car(user_data):
  for row in user_data:
    print(row)
  id = input('For which id you want to create a car?')
  sql_query = "INSERT INTO cars (car, model, car_year, car_number, user_id) VALUES "
  columns = ['car *', 'car_model *', 'car_year *', 'car_number *']
  car_data = []

  for column in columns:
    value = input(f'What is your {column} ? ')
    car_data.append(value)


  car_data.append(id)

  return sql_query + str(tuple(car_data))


def update_car(car_data):

  for row in car_data:
    print(row)

  info_keys = ['id', 'column name (car, model, car_year, car_number)', 'value']
  required_info = []

  for key in info_keys:
    value = input(f'Which {key} ? ')
    required_info.append(value)

  sql_query = f"UPDATE cars SET {required_info[1]} = '{required_info[2]}'  WHERE id = {required_info[0]};"

  return sql_query

def delete_car(car_data):
  for row in car_data:
    print(row)
  must_removed_id = input('Write the id of the one that should be deleted? ')
  sql_query = f'DELETE FROM cars WHERE id = {must_removed_id}'

  return sql_query


def list_car(cars_data):
  pages = math.ceil(len(cars_data) / 10)

  while True:
    needed_page = input(f'Which page do you want to see? (pages count, {pages})')

    if needed_page == 'exit':
      break

    try:
      needed_page = int(needed_page)
    except ValueError:
      print("Invalid input. Please enter a valid page number or 'exit'.")
      continue

    if needed_page > pages:
      print('There is no such page')
      continue

    for row in cars_data[(needed_page - 1) * 10: needed_page * 10]:
      print(row)


