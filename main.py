import sqlite3



def create_account(connection, name, initial_deposit=0.0):
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO banking (name, balance) VALUES (?, ?)",
        (name, initial_deposit)
    )
    account_id = cursor.lastrowid

    # Record initial deposit as a transaction
    if initial_deposit > 0:
        cursor.execute(
            "INSERT INTO transactions (account_id, type, amount) VALUES (?, ?, ?)",
            (account_id, "deposit", initial_deposit)
        )

    connection.commit()
    return account_id
    

def deposit(connection, account_id, amount):
    if amount <= 0:
        return False

    cursor = connection.cursor()

    cursor.execute("SELECT balance FROM banking WHERE id = ?", (account_id,))
    result = cursor.fetchone()
    if result is None:
        return False

    cursor.execute(
        "UPDATE banking SET balance = balance + ? WHERE id = ?",
        (amount, account_id)
    )

    cursor.execute(
        "INSERT INTO transactions (account_id, type, amount) VALUES (?, ?, ?)",
        (account_id, "deposit", amount)
    )

    connection.commit()
    return True


def withdraw(connection, account_id, amount):
    if amount <= 0:
        return False

    cursor = connection.cursor()

    cursor.execute("SELECT balance FROM banking WHERE id = ?", (account_id,))
    result = cursor.fetchone()
    if result is None:
        return False

    balance = result[0]

    if amount > balance:
        return False

    cursor.execute(
        "UPDATE banking SET balance = balance - ? WHERE id = ?",
        (amount, account_id)
    )

    cursor.execute(
        "INSERT INTO transactions (account_id, type, amount) VALUES (?, ?, ?)",
        (account_id, "withdrawal", amount)
    )

    connection.commit()
    return True

def check_balance(connection, account_id):
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM banking WHERE id = ?", (account_id,))
    result = cursor.fetchone()
    return result[0] if result else None

def list_accounts(connection):
    cursor = connection.cursor()

    results = cursor.execute("SELECT * FROM banking")

    print("\nAll Accounts:")
    for row in results:
        print(row)

def main():
    connection = sqlite3.connect('example.db')

    while True:
        print("\n--- Banking App ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. List Accounts")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            balance = float(input("Initial deposit: "))
            create_account(connection, name, balance)
            connection.commit()

        elif choice == "2":
            account_id = int(input("Account ID: "))
            amount = float(input("Amount to deposit: "))
            deposit(connection, account_id, amount)

        elif choice == "3":
            account_id = int(input("Account ID: "))
            amount = float(input("Amount to withdraw: "))
            withdraw(connection, account_id, amount)

        elif choice == "4":
            account_id = int(input("Account ID: "))
            balance = check_balance(connection, account_id)
    
            if balance is None:
                print("Account not found.")
            else:
                print(f"Balance: ${balance:.2f}")

        elif choice == "5":
            list_accounts(connection)

        elif choice == "6":
            break

        else:
            print("Invalid choice.")

    connection.close()


if __name__ == "__main__":
    main()
