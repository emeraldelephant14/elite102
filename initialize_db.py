import sqlite3

DB_NAME = 'example.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS banking
            (id integer primary key, 
            name text, 
            age integer, 
            balance real)
    ''')

    print("Table created.")

    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO banking (name, age, balance) VALUES
        ('Charlie', 18, 350),
        ('Mary', 28, 3.8),
        ('Catherine', 25, 100.9)
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


initialize_database()
