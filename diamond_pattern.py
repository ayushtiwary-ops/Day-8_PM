"""Diamond Pattern Printer -- Part C AI-Augmented Task.

Day 8 PM | IIT Gandhinagar PG Diploma AI-ML

--- PART C DOCUMENTATION ---

Prompt used:
"Write a Python program that prints a diamond pattern of asterisks.
The user inputs the number of rows for the upper half. Include proper
spacing and use nested loops only (no string multiplication tricks)."

What the AI got right:
- Basic upper/lower half structure using two for loops
- range() direction was correct (ascending for upper, descending for lower)
- Core logic of (spaces, then stars) per row was right

What the AI got wrong or missed:
1. Used print(" " * spaces) -- that IS string multiplication. The prompt
   explicitly said no string tricks. Fixed with inner for loops.
2. Off-by-one in lower half spacing: AI used (n - i) instead of (n - i)
   which was actually fine, but the star count used range(2*i) instead
   of range(2*i - 1), making each lower row one star too wide.
3. n=0 not handled -- range(1, 1) is empty for upper, but range(0, 0, -1)
   silently produces nothing for lower, giving no error but also no output.
4. n=1 printed a single star -- correct, but AI comment said it would print
   three rows, which was wrong documentation.
5. No time complexity mentioned anywhere. This is O(n^2).

This version fixes all five issues.
"""


def print_diamond(n):
    """Print a diamond with n rows in the upper half using nested for loops.

    No string multiplication used anywhere -- all repetition via inner loops.
    Time complexity: O(n^2).

    Args:
        n (int): Upper half row count (including middle row).
    """
    if n <= 0:
        print("  n must be >= 1. Nothing to print.")
        return

    # Upper half (rows 1 to n, widths 1, 3, 5, ..., 2n-1)
    for i in range(1, n + 1):
        for _ in range(n - i):       # leading spaces
            print(" ", end="")
        for _ in range(2 * i - 1):   # asterisks
            print("*", end="")
        print()

    # Lower half (mirror, rows n-1 down to 1)
    for i in range(n - 1, 0, -1):
        for _ in range(n - i):       # leading spaces
            print(" ", end="")
        for _ in range(2 * i - 1):   # asterisks
            print("*", end="")
        print()


def main():
    """Run the diamond printer."""
    print("")
    print("=" * 36)
    print("   DIAMOND PATTERN PRINTER")
    print("   Nested loops only -- no string tricks")
    print("=" * 36)

    while True:
        try:
            n = int(input("\n  Enter upper half rows (1-15): "))
            if 1 <= n <= 15:
                break
            print("  Please enter 1 to 15.")
        except ValueError:
            print("  Enter a whole number.")

    print("")
    print_diamond(n)
    print("")
    print("  n={}  |  Total rows: {}  |  O(n^2) time".format(n, 2 * n - 1))


if __name__ == "__main__":
    main()
