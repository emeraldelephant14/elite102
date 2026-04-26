import unittest
import sqlite3
from main import create_account, deposit, withdraw, check_balance

class TestBanking(unittest.TestCase):

    def setUp(self):
        # Fresh database for every test
        self.connection = sqlite3.connect(":memory:")
        cursor = self.connection.cursor()

        cursor.execute('''
            CREATE TABLE banking (
                id INTEGER PRIMARY KEY,
                name TEXT,
                balance REAL
            )
        ''')

        cursor.execute('''
            CREATE TABLE transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_id INTEGER,
                type TEXT,
                amount REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        self.connection.commit()

    def tearDown(self):
        self.connection.close()

    # ---- TESTS ----

    def test_create_account(self):
        acc_id = create_account(self.connection, "Alice", 100)

        balance = check_balance(self.connection, acc_id)
        self.assertEqual(balance, 100)

    def test_deposit(self):
        acc_id = create_account(self.connection, "Bob", 50)

        result = deposit(self.connection, acc_id, 30)
        self.assertTrue(result)

        balance = check_balance(self.connection, acc_id)
        self.assertEqual(balance, 80)

    def test_withdraw(self):
        acc_id = create_account(self.connection, "Charlie", 100)

        result = withdraw(self.connection, acc_id, 40)
        self.assertTrue(result)

        balance = check_balance(self.connection, acc_id)
        self.assertEqual(balance, 60)

    def test_withdraw_insufficient(self):
        acc_id = create_account(self.connection, "Dana", 20)

        result = withdraw(self.connection, acc_id, 100)
        self.assertFalse(result)

    def test_negative_deposit(self):
        acc_id = create_account(self.connection, "Eve", 50)

        result = deposit(self.connection, acc_id, -10)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()