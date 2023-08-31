import math

def detail_controller(users_data, details_data):
  action = input('What action do you want to take? (create, update, delete, list) ').lower().strip()

  if action == 'create':
    callback_value = create_details(users_data,details_data)
  elif action == 'update':
    callback_value = update_details(details_data)
  elif action == 'delete':
    callback_value = delete_details(details_data)
  elif action == 'list':
    callback_value = list_details(details_data)
  else:
    raise Exception('ERROR: No such action')

  return callback_value


def create_details(user_data, details_data):
  for row in user_data:
    print(row)

  id = input('For which id you want to create a details?')

  for detail in details_data:
      if id == detail[len(detail) - 1]:
          raise Exception('Error: This user already has details')

  sql_query = "INSERT INTO users_details (weight, height, eyes_color, user_id) VALUES "
  columns = ['weight *', 'height *', 'eyes_color *']
  details_data = []


  for column in columns:
    value = input(f'What is your {column} ? ')
    details_data.append(value)


  details_data.append(id)

  return sql_query + str(tuple(details_data))


def update_details(details_data):

  for row in details_data:
    print(row)

  info_keys = ['id', 'column name (weight, height, eyes_color)', 'value']
  required_info = []

  for key in info_keys:
    value = input(f'Which {key} ? ')
    required_info.append(value)

  sql_query = f"UPDATE users_details SET {required_info[1]} = '{required_info[2]}'  WHERE id = {required_info[0]};"

  return sql_query

def delete_details(details_data):
  for row in details_data:
    print(row)
  must_removed_id = input('Write the id of the one that should be deleted? ')
  sql_query = f'DELETE FROM users_details WHERE id = {must_removed_id}'

  return sql_query


def list_details(details_data):
  pages = math.ceil(len(details_data) / 10)

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

    for row in details_data[(needed_page - 1) * 10: needed_page * 10]:
      print(row)
