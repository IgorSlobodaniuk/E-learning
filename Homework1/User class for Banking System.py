class User(object):
    """
    Link to task:  https://www.codewars.com/kata/5a03af9606d5b65ff7000009
    """
    
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    
    def _is_enough_to_withdraw(self, balance, cash):
        return balance-cash >= 0 
    
    def _validate_input(self, cash):
        if not isinstance(cash, int) or cash < 0:
            raise ValueError('Incorrect cash value')

    def withdraw(self, cash):
        self._validate_input(cash)
        if self._is_enough_to_withdraw(self.balance, cash) is False:
            raise ValueError(f'{self.name} can\'t withdraw {cash}, he only has {self.balance}.')
                            
        self.balance -= cash
        return f'{self.name} has {self.balance}.'
    
    def check(self, user, cash):
        self._validate_input(cash)
        if user.checking_account is False:
            raise ValueError(f'{self.name}\'s checking account is disabled.')
        
        if self.checking_account is False:
            raise ValueError(f'{user.name}\'s checking account is disabled.')
            
        self.balance += cash
        user.balance -= cash
        return f'{self.name} has {self.balance} and {user.name} has {user.balance}.'
    
    def add_cash(self, cash):
        self._validate_input(cash)
        self.balance += cash
        return f'{self.name} has {self.balance}.'
