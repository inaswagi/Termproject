#Personal Financial Tracker

#Ismail Naswagi
#Bachelor of Science in Cybersecurity
#IT215-8, 2261B18
#Unit 7 Final Python Project

import json
from datetime import datetime

# -----------------------------
# Class Definition (OOP)
# -----------------------------
class Transaction:
    def __init__(self, amount, category, description, date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

# -----------------------------
# Function 1: Add Transaction
# -----------------------------
def add_transaction(transactions):
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food, Rent, etc.): ")
        description = input("Enter description: ")

        transaction = Transaction(amount, category, description)
        transactions.append(transaction)

        print("✅ Transaction added successfully!")

    except ValueError:
        print("❌ Invalid amount. Please enter a numeric value.")

# -----------------------------
# Function 2: View Transactions
# -----------------------------
def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return

    print("\n--- Transaction History ---")
    for i, t in enumerate(transactions, start=1):
        print(f"{i}. {t.date} | ${t.amount:.2f} | {t.category} | {t.description}")

# -----------------------------
# Function 3: Save to File
# -----------------------------
def save_to_file(transactions, filename="transactions.json"):
    try:
        with open(filename, "w") as file:
            json.dump([t.to_dict() for t in transactions], file, indent=4)
        print("💾 Data saved successfully!")

    except Exception as e:
        print(f"❌ Error saving file: {e}")

# -----------------------------
# Function 4: Load from File
# -----------------------------
def load_from_file(filename="transactions.json"):
    transactions = []
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            for item in data:
                t = Transaction(
                    item["amount"],
                    item["category"],
                    item["description"],
                    item["date"]
                )
                transactions.append(t)
        print("📂 Data loaded successfully!")

    except FileNotFoundError:
        print("⚠️ No existing file found. Starting fresh.")

    except json.JSONDecodeError:
        print("❌ File is corrupted. Starting fresh.")

    return transactions

# -----------------------------
# Function 5: Show Summary
# -----------------------------
def show_summary(transactions):
    if not transactions:
        print("No transactions to summarize.")
        return

    total = sum(t.amount for t in transactions)
    categories = {}

    for t in transactions:
        categories[t.category] = categories.get(t.category, 0) + t.amount

    print("\n--- Summary ---")
    print(f"Total Balance: ${total:.2f}")

    print("\nSpending by Category:")
    for category, amount in categories.items():
        print(f"{category}: ${amount:.2f}")

# -----------------------------
# Main Function
# -----------------------------
def main():
    transactions = load_from_file()

    while True:
        print("\n==== Personal Finance Tracker ====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Summary")
        print("4. Save Data")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(transactions)

        elif choice == "2":
            view_transactions(transactions)

        elif choice == "3":
            show_summary(transactions)

        elif choice == "4":
            save_to_file(transactions)

        elif choice == "5":
            save_to_file(transactions)
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")

# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    main()