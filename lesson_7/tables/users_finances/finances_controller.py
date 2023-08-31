import math

def finance_controller(users_data, finance_data):
  action = input('What action do you want to take? (create, update, delete, list) ').lower().strip()

  if action == 'create':
    callback_value = create_finance(users_data, finance_data)
  elif action == 'update':
    callback_value = update_finance(finance_data)
  elif action == 'delete':
    callback_value = delete_finance(finance_data)
  elif action == 'list':
    callback_value = list_finance(finance_data)
  else:
    raise Exception('ERROR: No such acfinance')
  return callback_value


def create_finance(user_data, finance_data):
  for row in user_data:
    print(row)

  id = input('For which id you want to create a finance?')

  sql_query = "INSERT INTO users_finances (salary, bonus, user_id) VALUES "
  columns = ['salary *', 'bonus *']
  fin_data = []


  for column in columns:
    value = input(f'What is your {column} ? ')
    fin_data.append(value)


  fin_data.append(id)

  return sql_query + str(tuple(fin_data))


def update_finance(finance_data):

  for row in finance_data:
    print(row)

  info_keys = ['id', 'column name (salary, bonus)', 'value']
  required_info = []

  for key in info_keys:
    value = input(f'Which {key} ? ')
    required_info.append(value)

  sql_query = f"UPDATE users_finances SET {required_info[1]} = '{required_info[2]}'  WHERE id = {required_info[0]};"

  return sql_query

def delete_finance(finance_data):
  for row in finance_data:
    print(row)
  must_removed_id = input('Write the id of the one that should be deleted? ')
  sql_query = f'DELETE FROM users_finances WHERE id = {must_removed_id}'

  return sql_query


def list_finance(finance_data):
  pages = math.ceil(len(finance_data) / 10)

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

    for row in finance_data[(needed_page - 1) * 10: needed_page * 10]:
      print(row)
