# Python OOPs Projects 🚀

Welcome to the **Python-OOPS-Project** repository! This collection contains various mini-projects designed to demonstrate and practice Object-Oriented Programming (OOP) concepts in Python.

## 📁 Projects Overview

### 1. Bank Account Management System (`Bank_Account.py`)
A simulation of a banking system that handles accounts, deposits, and withdrawals using classes and objects.
- **Features:**
  - Secure account key generation based on account name and number.
  - Validation for 12-digit account numbers and balance restrictions (e.g., Savings account max limit).
  - Debit (Withdraw) and Credit (Deposit) functionalities securely tied to an account key.
  - Data persistence: Stores and updates account information seamlessly in a CSV file (`Account.csv`).
- **Concepts used:** Encapsulation, static methods, class instances, CSV file handling, exception handling.

### 2. Kaun Banega Crorepati (KBC) Game (`KBC.py`)
A command-line trivia game inspired by the popular television show *Kaun Banega Crorepati*.
- **Features:**
  - Multiple-choice questions with increasing prize money.
  - Interactive command-line interface.
  - Immediate feedback on answers and total winnings calculation (Up to ₹50,000!).
- **Concepts used:** Class-based game state management, lists for questions/options, user input handling, conditional logic.

### 3. Expense Tracker (`expenses.py`)
A personal finance manager to track your daily expenses, powered by a SQLite database.
- **Features:**
  - **Add Expenses:** Log new expenses with amount, category, date, and optional notes.
  - **View & Search:** Display all expenses or search by specific categories.
  - **Update & Delete:** Modify existing records or delete erroneous entries.
  - **Summary:** View total spending grouped by category.
  - Data persistence: Uses `sqlite3` to store data securely in `expenses.db`.
- **Concepts used:** Database integration (`sqlite3`), CRUD operations, destructors (`__del__`), exception handling, grouping and aggregation.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries/Modules:**
  - `csv` (for Bank Account system)
  - `sqlite3` (for Expense Tracker)
  - `datetime` (for Expense Tracker)

## 🚀 Setup & Execution

### Prerequisites
Make sure you have [Python 3](https://www.python.org/downloads/) installed on your system. No external pip packages are required as all modules used are part of the standard Python library.

### Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Python-OOPS-Project
   ```

2. **Run the Bank Account Project:**
   ```bash
   python Bank_Account.py
   ```
   *(Note: Modify the `Bank_Account.py` file to create your own account objects at the bottom of the script for testing.)*

3. **Play the KBC Game:**
   ```bash
   python KBC.py
   ```
   Follow the on-screen prompts to answer questions!

4. **Run the Expense Tracker:**
   ```bash
   python expenses.py
   ```
   Uncomment the methods at the bottom of the `expenses.py` file to test adding, showing, or updating entries.

## 💡 Future Enhancements (Bonus Ideas)
- Export expense data to a CSV file.
- Add visualizations for expenses using Matplotlib or Plotly.
- Build graphical user interfaces (GUI) or web UIs using Flask/Django.
- Add unit tests for robust code validation.

---
*Happy Coding! 💻*
