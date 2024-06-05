import unittest
from main import BankAccount


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("1234567890")

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 0.0)

    def test_deposit(self):
        self.account.deposit(100.0)
        self.assertEqual(self.account.get_balance(), 100.0)

    def test_withdraw(self):
        self.account.deposit(100.0)
        self.account.withdraw(50.0)
        self.assertEqual(self.account.get_balance(), 50.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(50.0)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-10.0)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(-10.0)

    def test_withdraw_exact_balance(self):
        self.account.deposit(100.0)
        self.account.withdraw(100.0)
        self.assertEqual(self.account.get_balance(), 0.0)


if __name__ == "__main__":
    unittest.main()
