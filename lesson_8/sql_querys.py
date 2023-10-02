sql_request_data = "SELECT users.id, users.first_name, users.last_name, card.card_number, card.amount FROM users INNER JOIN card ON users.id = card.user_id;"
sql_add_info_transactions = "insert into transactions(money, from_user, to_user, is_success) values "

sql_card_amount_change = "update card set amount = '{}' where user_id = '{}' ;"

