import sqlite3
from datetime import datetime

class Expenses:
    def __init__(self):
        try:
            self.connect_db = sqlite3.connect('expenses.db')
            self.cursor = self.connect_db.cursor()
            create_query = f'''
            CREATE TABLE IF NOT EXISTS EXPENSES (
                ID INTEGER PRIMARY KEY,
                AMOUNT REAL NOT NULL,
                CATEGORY TEXT NOT NULL,
                DATE DATE NOT NULL,
                NOTE TEXT
            )
            '''
            self.cursor.execute(create_query)
            self.connect_db.commit()
            
        except Exception as e:
            print('Table creation failed', e)
        else:
            print('Table EXPENSES Exists\n')

    def add_to_db(self):
        try:
            print("Enter your details")
            try:
                amt = float(input("Enter amount: "))
            except ValueError:
                print("Invalid amount")
            ctg = input("Enter category: ")
            date = input("Enter date(DD-MM-YYYY): ")
            date = datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")
            note = input("Enter note(press 'enter' to skip): ")
            if note == '':
                note = None
            insert_query = f'''
            INSERT INTO EXPENSES (AMOUNT , CATEGORY , DATE , NOTE) VALUES (?, ?, ?, ?)
            '''
            self.cursor.execute(insert_query, (amt, ctg, date, note))
            self.connect_db.commit()
        except Exception as e:
            print("Data insertion failed", e)
        else:
            print("Data inserted Successfully")

    def show_db(self):
        try:
            select_query = f'SELECT * FROM EXPENSES'
            self.cursor.execute(select_query)
            data = self.cursor.fetchall()
            self.cursor.execute("SELECT COUNT(*) FROM EXPENSES")
            for row in data:
                print(row)
        except Exception as e:
            print("Error fetching data", e)

    def __del__(self):
        self.connect_db.close()
        print("\nDatabase connection Closed!")

    def update_value(self):
        try:
            C_N = input("Enter column name(in capital): ")
            value = input("Enter value: ")
            if value == '':
                value = None
            id = int(input("Enter id where to update: "))
            update_query = f'UPDATE EXPENSES SET {C_N}  = ? WHERE ID = ?'
            self.cursor.execute(update_query, (value,id))
            self.connect_db.commit()
        except Exception as e:
            print("Error updating value", e)
        else:
            print("Value updated Successfully")

    def summary(self):
        self.cursor.execute("SELECT CATEGORY, SUM(AMOUNT) FROM EXPENSES GROUP BY CATEGORY")
        for row in self.cursor.fetchall():
            print(f"{row[0]}: ₹{row[1]}")

    def delete_entry(self):
        id = int(input("Enter ID to delete: "))
        self.cursor.execute("DELETE FROM EXPENSES WHERE ID = ?", (id,))
        self.connect_db.commit()
        print("Entry deleted.")
    
    def search(self):
        category = input("Enter category to search: ")
        self.cursor.execute("SELECT * FROM EXPENSES WHERE CATEGORY = ?", (category,))
        for row in self.cursor.fetchall():
            print(row)
    
e1 = Expenses()
# e1.add()
# e1.show_db()
# e1.update_value()
del e1


'''
Bonus Ideas that can be implemented:
- Export to CSV
- Add charts using matplotlib or plotly
- Build a simple web UI with Flask or Django
- Add unit tests using unittest or pytest
'''