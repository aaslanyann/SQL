import math

def user_controller(users_data):
  action = input('What action do you want to take? (create, update, delete, list) ').lower().strip()

  if action == 'create':
    callback_value = create_user()
  elif action == 'update':
    callback_value = update_user(users_data)
  elif action == 'delete':
    callback_value = delete_user(users_data)
  elif action == 'list':
    callback_value = list_users(users_data)
  else:
    raise Exception('ERROR: No such action')

  return callback_value

def create_user():
  sql_query = "INSERT INTO users (first_name, last_name, email, age, country) VALUES "
  columns = ['first_name *', 'last_name *', 'email *', 'age *', 'country *']
  user_data = []

  for column in columns:
    value = input(f'What is your {column} ? ')
    user_data.append(value)



  return sql_query + str(tuple(user_data))


def update_user(user_data):

  for row in user_data:
    print(row)

  info_keys = ['id', 'column name (first_name, last_name, email, age, country)', 'value']
  required_info = []

  for key in info_keys:
    value = input(f'Which {key} ? ')
    required_info.append(value)

  sql_query = f"UPDATE users SET {required_info[1]} = '{required_info[2]}'  WHERE id = {required_info[0]};"

  return sql_query

def delete_user(users_data):
  for row in users_data:
    print(row)
  must_removed_id = input('Write the id of the one that should be deleted? ')
  sql_query = f'DELETE FROM users WHERE id = {must_removed_id}'

  return sql_query


def list_users(users_data):
  pages = math.ceil(len(users_data) / 10)

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

    for row in users_data[(needed_page - 1) * 10: needed_page * 10]:
      print(row)
