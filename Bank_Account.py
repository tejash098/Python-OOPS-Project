import csv

class Bank_account:
    @staticmethod
    def validate_acc_no(n):
        if len(str(n)) == 12:
            return n
        else:
            raise Exception('Account number should be of 12 digits')
    
    def validate_bal(self, bal):
        if self.Accont_type == 'saving' and bal > 100000:
            raise Exception('This is a saving account, Balance should be below 1 lakh')
        else:
            return bal

    def info(self):
        print(self.__dict__)

    def check_balance(self):
        print(f'Current available balance is Rs.{self.Balance}')
    
    def pass_key(self):
        return self.Name[:2]+str(self.Accont_No)[:3]
    
    def get_key(self):
        print(f'This is your Account Key: {self.__Key} \nDo not share with anyone!')

    def __init__(self, name, number, acc_type, balance=0):
        self.Name = name
        self.Accont_No = self.validate_acc_no(number)
        self.Accont_type = acc_type
        self.Balance = self.validate_bal(balance)
        self.__Key = self.pass_key()
        self.save()

    def save(self):
        try:
            with open('Account.csv', 'r', newline='') as file:
                reader = csv.reader(file)
                records = list(reader)
        except FileNotFoundError:
            records = []

        for row in records:
            if len(row) > 1 and str(self.Accont_No) == str(row[1]):
                return

        with open('Account.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.Name, self.Accont_No, self.Accont_type, self.Balance])

    def __update_csv_balance(self):
        with open('Account.csv', 'r', newline='') as file:
            data = csv.reader(file)
            rows = list(data)

        for i in range(len(rows)): 
            if str(rows[i][1]) == str(self.Accont_No):
                rows[i][3] = str(self.Balance)

        with open('Account.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

    def credit(self, amt):
        no = input('Enter your Key: ')
        if str(no) == str(self.__Key):
            new_balance = self.Balance + amt
            self.Balance = self.validate_bal(new_balance)
            print(f'Balance updated: Rs.{self.Balance}-/-')
            self.__update_csv_balance()
        else:
            raise Exception('Invalid Key')

    def debit(self, amt):
        no = input('Enter your Key: ')
        if str(no) == str(self.__Key):
            if amt <= self.Balance:
                new_balance = self.Balance - amt
                self.Balance = self.validate_bal(new_balance)
                print(f'Balance updated: Rs.{self.Balance}-/-')
                self.__update_csv_balance()
            else:
                raise Exception('Low Balance!')
        else:
            raise Exception('Invalid Key')

acc1 = Bank_account('demo_name', 987456321987, 'saving', 5000)
acc1.get_key()
acc1.credit(2000)
acc1.info()
acc1.debit(4500)
acc1.info()
