"""
This module defines BankAccount class, which supports
basic banking operations such as deposits, withdrawals,
and balance checks.
"""
class BankAccount:
    """A bank account class with attributes for account holder name and balalnce. 
    Also includes methods for deposits, withdrawal and balance retrieval."""

    def __init__(self, customer_name, balance=0):
        """ Initialize a new bank account. Parameters: name: The account holder's name. 
        balance: Starting balance (default is 0). """
        self.name = customer_name
        self.balance = balance

    def deposit(self, funds):
        """ Add funds to the account balance. Parameters: funds: The amount to deposit. """
        self.balance += funds
        print("Success: Deposit completed.")

    def withdraw(self, funds):
        """ Remove funds from the account if enough funds exist. 
        Parameters: funds: The amount to withdraw. """
        if funds > self.balance:
            print("Error: Not enough funds to withdraw.")
        else:
            self.balance -= funds
            print("Success: Withdrawal completed.")

    def get_balance(self):
        """Return the current account balance.

        Returns: The current balance."""
        return self.balance
