from datetime import datetime
from decimal import Decimal

from transactions import Transaction, Category
from database import init_db, get_session


def create_category_if_not_exists(session, category_name: str) -> Category:
    category = session.query(Category).filter_by(name=category_name).first()
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()  # Commit to get the ID assigned
    return category


def seed_database():
    # Initialize database and create tables
    init_db()

    # Get a session
    session = get_session()

    try:
        # Check if the category exists before adding it
        job_category = create_category_if_not_exists(session, "Job")
        groceries_category = create_category_if_not_exists(session, "Groceries")

        # Check if transactions exist, if not, create sample transactions
        existing_transactions = session.query(Transaction).first()
        if not existing_transactions:
            # Create sample transactions
            transactions = [
                Transaction(
                    date=datetime.now().isoformat(),
                    description="Salary",
                    amount=Decimal("5000"),
                    category_ref=job_category,
                ),
                Transaction(
                    date=datetime.now().isoformat(),
                    description="Freelance Project",
                    amount=Decimal("1500"),
                    category_ref=job_category,
                ),
                Transaction(
                    date=datetime.now().isoformat(),
                    description="PnP Groceries",
                    amount=Decimal("-2000"),
                    category_ref=groceries_category,
                ),
            ]

            # Add transactions to session
            for transaction in transactions:
                session.add(transaction)
            print("Created and added sample transactions to the database.")
            session.commit()
        else:
            print(
                "Transactions already exist in the database. No new transactions added."
            )

    finally:
        session.close()


if __name__ == "__main__":
    seed_database()
