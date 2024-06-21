import bank_account
import unittest

class TestBankAccount(unittest.TestCase):
    
    def test_initial_balance(self):
        self.assertEqual(bank_account.myBank.balance, 100)
    
    def setUp(self):
        self.account = bank_account.BankAccount(initial_balance=100)

    def tearDown(self):
        self.account = None

    def test_deposit_positive_amount(self):
        self.account.balance += 50

        self.assertEqual(self.account.balance, 150)

    def test_deposit_zero_amount(self):

        with self.assertRaises(ValueError):
            self.assertTrue(self.account.deposit(0))



if __name__ == '__main__':
    unittest.main()


