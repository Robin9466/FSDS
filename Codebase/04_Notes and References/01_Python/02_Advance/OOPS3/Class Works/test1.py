class Bank:

    def transacation(self):
        print(f'total transaction value')
    def account_opening(self):
        print(f'this will show your account open status')
    def deposit(self):
        print(f'this is show your deposited amount')

    class HDFC_bank(Bank):
        def hdfc_to_icici(self):
            print(f'this will show you all the transaction happened to icici through hdfc')
    class icici(HDFC_bank):
        pass

    i = icici()
    i.hdfc_to_icici()
    i.deposit()
    i.account_opening()