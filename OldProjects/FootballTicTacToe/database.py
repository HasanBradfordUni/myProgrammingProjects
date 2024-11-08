import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def getLastRow(connection):
    select_statement = """
SELECT id FROM FootballerClubs
ORDER BY id DESC
LIMIT 1;
"""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(select_statement)
        result = cursor.fetchone()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

def main():
    connection = create_connection(".\\sm_app.sqlite")

    create_clubs_table = """
CREATE TABLE IF NOT EXISTS FootballerClubs (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  club1 TEXT NOT NULL,
  club2 TEXT,
  club3 TEXT,
  club4 TEXT,
  club5 TEXT,
  club6 TEXT,
  club7 TEXT,
  nationality TEXT NOT NULL
);
"""

    execute_query(connection, create_clubs_table)

    insert_data(connection)

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def insert_data(connection):
    num = getLastRow(connection)
    print(num)
    num = num[0] + 1
    print(num)
    inputMore = True
    while inputMore:
        name = input("Enter footballer name: ")
        club1 = input("Enter first club: ")
        club2 = input("Enter second club: ")
        club3 = input("Enter third club: ")
        club4 = input("Enter fourth club: ")
        club5 = input("Enter fifth club: ")
        club6 = input("Enter sixth club: ")
        club7 = input("Enter seventh club: ")
        nationality = input("Enter nationality: ")
        insertStatement = f"""
INSERT INTO
  FootballerClubs(id, name, club1, club2, club3, club4, club5, club6, club7, nationality)
VALUES
  ('{int(num)}','{name}','{club1}','{club2}','{club3}','{club4}','{club5}','{club6}','{club7}','{nationality}');
"""
        execute_query(connection, insertStatement)
        inputMore = input("Do you wish to input more(Y/N): ")
        if inputMore == "Y":
            inputMore = True
        else:
            inputMore = False
        num += 1

if __name__ == "__main__":
    main()
