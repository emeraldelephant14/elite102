import sqlite3


def main():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Get all rows from the banking table
    print("Fetching all rows from the banking table...")
    results = cursor.execute('''
        SELECT * FROM banking
    ''')

    print("Results:")
    for row in results:
        print(row)

    
    print("Fetching people with balance greater than 200...")
    results = cursor.execute('''
        SELECT * FROM banking WHERE balance > 200
    ''')
    print("Results:")
    for row in results:
        print(row)

    print("Adding a new account")
    create_account('Akshaya', 17, 1000)
    new = cursor.execute('''
        SELECT * FROM banking
    ''')


    connection.close()

def create_account(name, age, balance):
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    cursor.execute('''
        INSERT INTO banking (name, age, balance) VALUES (?, ?, ?)
    ''', (name, age, balance))

    connection.commit()
    connection.close()
    print(f"Account created for {name} with balance {balance}")
    

def deposit(): 
    pass

def withdraw():
    pass

if __name__ == "__main__":
    main()
