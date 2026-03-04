"""Daily Transaction Analyzer -- Part D Bonus."""

HIGH_VALUE_THRESHOLD = 10000
BAR_UNIT = 1000
VALID_CATEGORIES = ("food", "travel", "bills", "other")
VALID_TYPES = ("credit", "debit")

def get_transaction():
    raw = input("  Amount (or done to finish): ").strip().lower()
    if raw == "done": return None
    try:
        amount = float(raw)
        if amount <= 0: print("  Positive only."); return "skip"
    except ValueError:
        print("  Invalid."); return "skip"
    while True:
        t = input("  Type (credit/debit): ").strip().lower()
        if t in VALID_TYPES: break
        print("  credit or debit only.")
    while True:
        cat = input("  Category (food/travel/bills/other): ").strip().lower()
        if cat in VALID_CATEGORIES: break
        print("  food, travel, bills, or other.")
    high = amount > HIGH_VALUE_THRESHOLD
    if high: print("  [HIGH VALUE] Rs {:,.0f}".format(amount))
    return {"amount": amount, "type": t, "category": cat, "high_value": high}


def print_bar_chart(transactions):
    """Print bar chart for last 10 transactions. Each * = Rs 1,000.

    Uses a for loop with enumerate over the last-10 slice.

    Args:
        transactions (list): All collected transactions.
    """
    last_ten = transactions[-10:]
    print("\n  Bar Chart -- last {} transactions  (* = Rs 1,000)".format(len(last_ten)))
    print("  " + "-" * 46)
    for i, txn in enumerate(last_ten, start=1):
        bars = max(int(txn["amount"] / BAR_UNIT), 1)
        symbol = "+" if txn["type"] == "credit" else "-"
        flag = " [HIGH]" if txn["high_value"] else ""
        print("  {:2}. [{}] Rs {:>9,.0f}  {}{}".format(
            i, symbol, txn["amount"], "*" * bars, flag
        ))


def print_summary(transactions):
    """Print full analytics summary with category breakdown.

    Args:
        transactions (list): All collected transactions.
    """
    if not transactions:
        print("  No transactions recorded.")
        return

    total_credits = sum(t["amount"] for t in transactions if t["type"] == "credit")
    total_debits = sum(t["amount"] for t in transactions if t["type"] == "debit")
    net_balance = total_credits - total_debits
    all_amounts = [t["amount"] for t in transactions]
    highest = max(all_amounts)
    average = sum(all_amounts) / len(all_amounts)
    high_value_count = sum(1 for t in transactions if t["high_value"])

    # category breakdown using a dictionary
    category_totals = {cat: 0.0 for cat in VALID_CATEGORIES}
    for txn in transactions:
        category_totals[txn["category"]] += txn["amount"]

    print("\n" + "=" * 48)
    print("  TRANSACTION SUMMARY")
    print("=" * 48)
    print("  Total Transactions : {}".format(len(transactions)))
    print("  Total Credits      : Rs {:,.2f}".format(total_credits))
    print("  Total Debits       : Rs {:,.2f}".format(total_debits))
    print("  Net Balance        : Rs {:,.2f}".format(net_balance))
    print("  Highest Transaction: Rs {:,.2f}".format(highest))
    print("  Average Amount     : Rs {:,.2f}".format(average))
    print("  High Value (>10K)  : {}".format(high_value_count))
    print("\n  Spending by Category:")
    for cat, total in category_totals.items():
        if total > 0:
            print("    {:10}: Rs {:,.2f}".format(cat, total))
    print("=" * 48)


def main():
    """Run the transaction analyzer dashboard."""
    print("")
    print("=" * 48)
    print("   SMART TRANSACTION ANALYZER")
    print("   Paytm Mini Analytics Dashboard")
    print("=" * 48)
    print("\n  Enter transactions one by one.")
    print("  Type done when finished.\n")

    transactions = []

    # while loop: keep collecting until user types done
    while True:
        result = get_transaction()
        if result is None:       # user typed done -- break
            break
        if result == "skip":     # invalid input -- continue to next iteration
            continue
        transactions.append(result)
        print("  Recorded. Total so far: {}".format(len(transactions)))

    if not transactions:
        print("\n  No transactions entered. Exiting.")
        return

    print_bar_chart(transactions)
    print_summary(transactions)


if __name__ == "__main__":
    main()