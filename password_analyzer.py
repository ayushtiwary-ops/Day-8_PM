"""Password Strength Analyzer and Generator.

Day 8 PM -- for loops, while loops, break, continue, loop-else.
IIT Gandhinagar | PG Diploma AI-ML & Agentic AI Engineering

Usage:
    python password_analyzer.py
"""

import random
import string

SPECIAL_CHARS = "!@#$%^&*"
CHAR_POOL = string.ascii_letters + string.digits + string.punctuation


def get_strength_label(score):
    """Return a strength label for a given score (0-7)."""
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    elif score <= 6:
        return "Strong"
    return "Very Strong"


def analyze_password(password):
    """Score a password across 7 criteria.

    Scoring:
        Length >= 8  -> +1, >= 12 -> +2, >= 16 -> +3
        Has uppercase -> +1
        Has lowercase -> +1
        Has digit     -> +1
        Has special   -> +1
        No 3+ consecutive repeats -> +1

    Returns:
        tuple: (score, missing list, breakdown dict)
    """
    score = 0
    missing = []
    breakdown = {}

    # -- Length --
    length = len(password)
    if length >= 16:
        score += 3
        breakdown["length"] = "Length >= 16 chars (+3)  [PASS]"
    elif length >= 12:
        score += 2
        breakdown["length"] = "Length >= 12 chars (+2)  [PASS]"
    elif length >= 8:
        score += 1
        breakdown["length"] = "Length >= 8 chars (+1)   [PASS]"
    else:
        breakdown["length"] = "Length {} chars (need >= 8)  [FAIL]".format(length)
        missing.append("too short")

    # -- Character types via for loop --
    has_upper = has_lower = has_digit = has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
        if ch in SPECIAL_CHARS:
            has_special = True

    if has_upper:
        score += 1
        breakdown["uppercase"] = "Has uppercase  [PASS]"
    else:
        missing.append("uppercase letter")
        breakdown["uppercase"] = "No uppercase   [FAIL]"

    if has_lower:
        score += 1
        breakdown["lowercase"] = "Has lowercase  [PASS]"
    else:
        missing.append("lowercase letter")
        breakdown["lowercase"] = "No lowercase   [FAIL]"

    if has_digit:
        score += 1
        breakdown["digit"] = "Has digit      [PASS]"
    else:
        missing.append("digit")
        breakdown["digit"] = "No digit       [FAIL]"

    if has_special:
        score += 1
        breakdown["special"] = "Has special char  [PASS]"
    else:
        missing.append("special character (!@#$%^&*)")
        breakdown["special"] = "No special char   [FAIL]"

    # -- No 3+ consecutive repeated characters --
    has_triple = False
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            has_triple = True
            break

    if not has_triple:
        score += 1
        breakdown["repeats"] = "No 3+ repeated chars in a row  [PASS]"
    else:
        missing.append("3+ repeated chars in a row")
        breakdown["repeats"] = "Has 3+ repeated chars in a row [FAIL]"

    return score, missing, breakdown


def print_analysis(password, score, missing, breakdown, verbose=True):
    """Print formatted password strength report."""
    label = get_strength_label(score)
    if len(password) > 2:
        masked = password[0] + "*" * (len(password) - 2) + password[-1]
    else:
        masked = "**"

    print("")
    print("  Password  : {}".format(masked))
    print("  Score     : {}/7 ({})".format(score, label))

    if verbose:
        print("  Breakdown:")
        for val in breakdown.values():
            print("    - {}".format(val))

    if missing:
        print("  Missing   : {}".format(", ".join(missing)))


def generate_password(length):
    """Generate a random password using a for loop over range(length).

    Args:
        length (int): Desired password length.

    Returns:
        str: Generated password.
    """
    password = ""
    for _ in range(length):
        password += random.choice(CHAR_POOL)
    return password


def run_analyzer():
    """Prompt for passwords in a while loop until score >= 5."""
    print("\n--- Password Strength Analyzer ---")
    print("  Type 'skip' to exit.\n")

    while True:
        password = input("  Enter password: ").strip()

        if password.lower() == "skip":
            print("  Exiting.")
            break

        if not password:
            print("  Password cannot be empty.")
            continue

        score, missing, breakdown = analyze_password(password)
        print_analysis(password, score, missing, breakdown)

        if score >= 5:
            print("\n  Password accepted!\n")
            break

        print("\n  Try again -- need score >= 5...\n")


def run_generator():
    """Generate a password of user-specified length."""
    print("\n--- Password Generator ---")

    while True:
        try:
            length = int(input("  Length (8-64): "))
            if 8 <= length <= 64:
                break
            print("  Choose between 8 and 64.")
        except ValueError:
            print("  Enter a whole number.")

    generated = generate_password(length)
    score, missing, breakdown = analyze_password(generated)
    print("\n  Generated : {}".format(generated))
    print_analysis(generated, score, missing, breakdown, verbose=False)


def main():
    """Run the password tool menu."""
    print("")
    print("=" * 42)
    print("   PASSWORD STRENGTH TOOL")
    print("   IIT Gandhinagar -- AI-ML Diploma")
    print("=" * 42)

    while True:
        print("\n  1 -- Analyze a password")
        print("  2 -- Generate a password")
        print("  3 -- Exit")
        choice = input("\n  Choice: ").strip()

        if choice == "1":
            run_analyzer()
        elif choice == "2":
            run_generator()
        elif choice == "3":
            print("\n  Goodbye.\n")
            break
        else:
            print("  Enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
