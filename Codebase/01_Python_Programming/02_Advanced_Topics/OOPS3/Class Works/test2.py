class Bank:

    def transacation(self):
        print(f'total transaction value')
    def account_opening(self):
        print(f'this will show your account open status')
    def deposit(self):
        print(f'this is show your deposited amount')
    def test(self):
        print(f'this is a test method from bank class')

class HDFC_bank:
        def hdfc_to_icici(self):
            print(f'this will show you all the transaction happened to icici through hdfc')
        def test(self):
            print(f'this is a test method from hdfc bank')

class ineuron_bank:
    def account_status_icici(self):
        print(f'print a account status in icici')
class icici(HDFC_bank, Bank, ineuron_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.deposit()
i.transacation()
i.account_opening()
i.test()
i.account_status_icici()