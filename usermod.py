import sqlite3
database = './database/database.db'
connection = sqlite3.connect(database,check_same_thread=False) # create the file if it does not exist 
cursor = connection.cursor() # cursor is used to interact with the database 

def execute(statement):
    cursor.execute(statement) 
    connection.commit()

def drop(table_name):
    statement_drop = f"DROP TABLE IF EXISTS {table_name.upper()}" 
    execute(statement_drop) #  delete

def select(table_name, column_name="*"):
    rows = cursor.execute(f"SELECT {column_name} FROM {table_name}") 
    result = rows.fetchall()
    for row in rows:
        print(row[0])
    return result

def select_id(table_name, id, column_name="*"):
    rows = cursor.execute(f"SELECT {column_name} FROM {table_name} WHERE id = {id}")
    result = rows.fetchone()
    # print(result)
    return result

def update(table_name, column_name, value, condition):
    value = f"'{value}'"
    statement_update = f"UPDATE {table_name} SET {column_name} = {value} WHERE {condition}"
    # print(statement_update)
    execute(statement_update)

    
def create(table_name, column_name, value):
    print('create')
    username = value.split(",")[0]
    # check if the user already exists
    try:
        statement_create = f"INSERT INTO {table_name}({column_name}) VALUES ({value})"
        execute(statement_create)
    except sqlite3.IntegrityError:
        print(f"User {username} already exists")
        return False

def select_username(username, column_name="*"):
    rows = cursor.execute(f'SELECT {column_name} FROM account WHERE username = "{username}"') 
    result = rows.fetchone()
    # print(result)
    return result

def select_all(table_name, column_name="*"):
    rows = cursor.execute(f'SELECT {column_name} FROM {table_name}') 
    result = rows.fetchall()
    for row in result:
        print(row)
    return result

def delete(table_name, condition):
    condition = condition.split("=")
    condition = f"{condition[0]}='{condition[1]}'"
    statement_delete = f"DELETE FROM {table_name} WHERE {condition}"
    execute(statement_delete)

def create_account_table():
    # drop everything in the database before adding new tables
    drop("account")
    # statement to create a user table
    statement_account = """CREATE TABLE IF NOT EXISTS ACCOUNT
                (id  INTEGER PRIMARY KEY AUTOINCREMENT,
                username  TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                score INTEGER DEFAULT 0);"""
    # statement to insert an admin user in default
    statement_admin_insert = """INSERT INTO ACCOUNT(username,password,role,score) 
    VALUES ('admin','admin123','admin',0)"""
    # create table
    execute(statement_account)
    # insert admin user
    execute(statement_admin_insert)
    connection.close() # 关闭连接


