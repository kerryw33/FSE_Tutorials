from datetime import datetime
from decimal import Decimal
from sqlite3 import OperationalError

from transactions import Transaction, Category, calculate_financial_summary
from database import get_session


def main():
    # Initialize database and create tables
    # Get a session
    session = get_session()

    try:
        # Ensure transaction table exists by querying it
        session.query(Transaction).first()

        # Query all transactions from the database
        all_transactions = session.query(Transaction).all()

        # Calculate and display summary
        summary = calculate_financial_summary(all_transactions)
        print("Financial Summary:")
        for key, value in summary.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
    except Exception as e:
        print(f"You may need to seed the database first, run 'python seed.py' and try again.\n\n")
        raise e

    finally:
        session.close()
        #TODO: Once you have added the expense category and sample expenses, uncomment the lines below to display them!
        # display_transactions_by_category("Income")
        # display_transactions_by_category("Expense")


#TODO: Add the expense category if it does not exist, check if it exists first like we do above!
def add_expense_category():
    session = get_session()
    try:
        pass
    finally:
        session.close()

#TODO: Add sample expenses if they do not exist
def add_expenses():
    session = get_session()
    try:
        pass
    finally:
        session.close()

def display_transactions_by_category(category_name: str):
    session = get_session()
    try:
        transactions = session.query(Transaction).filter_by(category=category_name).all()
        print(f"\nTransactions in category '{category_name}':")
        for t in transactions:
            print(t)
    finally:
        session.close()


if __name__ == "__main__":
    main()
