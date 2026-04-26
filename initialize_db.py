import sqlite3

DB_NAME = 'example.db'

def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")

    cursor.execute("DROP TABLE IF EXISTS banking")

    # a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS banking (
            id INTEGER PRIMARY KEY,
            name TEXT,
            balance REAL
        )
    ''')


    print("Table created.")

    # inserting sample data
    print("Inserting sample data...")
    cursor.execute("SELECT COUNT(*) FROM banking")
    count = cursor.fetchone()[0]
    if count == 0: #to remove duplicating
        cursor.execute('''
            INSERT INTO banking (name, balance) VALUES
            ('Charlie', 350),
            ('Mary', 3.8),
            ('Catherine', 100.9)
        ''')
    print("Sample data inserted.")
    #commit the changes and close the connection
    print("Committing changes and closing the connection...")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            type TEXT,
            amount REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    connection.commit()
    connection.close()


initialize_database()
