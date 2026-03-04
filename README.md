# Day 8 PM — Loops and Iteration

**IIT Gandhinagar | PG Diploma in AI-ML & Agentic AI Engineering**
Day 8 PM Take-Home Assignment | Due: 06/03/2026 07:15 PM

---

## Files

| File | Part | Description |
|---|---|---|
| `password_analyzer.py` | A | Password strength analyzer + generator |
| `diamond_pattern.py` | C | Diamond pattern printer — AI-generated, critiqued, improved |
| `transaction_analyzer.py` | D | Paytm-style transaction analytics dashboard (Bonus) |

Part B interview answers are below.

---

## How to Run

```bash
python password_analyzer.py      # Part A
python diamond_pattern.py        # Part C
python transaction_analyzer.py   # Part D (Bonus)
```

No external packages required.

---

## Part B — Interview Ready

### Q1: break vs continue, and loop-else

**break** exits the loop entirely the moment it is hit — no more iterations happen.
**continue** skips only the rest of the current iteration and jumps straight to the next one.

```python
# break -- stops the loop completely
for i in range(5):
    if i == 3:
        break
    print(i)
# Output: 0, 1, 2   (never reaches 3 or 4)

# continue -- skips one iteration, loop carries on
for i in range(5):
    if i == 3:
        continue
    print(i)
# Output: 0, 1, 2, 4   (3 is skipped, but 4 still runs)
```

**The else clause on loops:**
The `else` block on a `for` or `while` loop runs only if the loop completed
*without hitting a `break`*. If the loop was broken out of, else is skipped.

```python
for i in range(5):
    if i == 10:     # never true
        break
else:
    print("Loop finished normally")   # runs -- no break happened

for i in range(5):
    if i == 3:
        break       # triggered
else:
    print("This will NOT print")      # skipped because break ran
```

**Practical use case — search pattern:**
This is the cleanest way to check "did I find something?":

```python
def find_user(users, target):
    for user in users:
        if user == target:
            print("Found:", user)
            break
    else:
        print("User not found")   # only runs if we never broke out

find_user(["alice", "bob", "charlie"], "dave")
# Output: User not found
```

Without `else`, you would need a separate `found = False` flag variable,
which is messier and less Pythonic.

---

### Q2: find_pairs() — O(n²) and O(n)

**O(n²) version using nested loops:**

```python
def find_pairs(numbers, target):
    """Return all pairs that sum to target. O(n^2) time."""
    pairs = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):   # j starts at i+1 to avoid duplicates
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs

find_pairs([1, 2, 3, 4, 5], 6)
# Output: [(1, 5), (2, 4)]
```

**Why O(n²):** The outer loop runs n times. For each outer iteration, the inner
loop runs up to n-1 times. So worst case is n × n = n² comparisons.

**O(n) version using a set:**

```python
def find_pairs_fast(numbers, target):
    """Return all pairs that sum to target. O(n) time using a set."""
    seen = set()
    pairs = []
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

find_pairs_fast([1, 2, 3, 4, 5], 6)
# Output: [(1, 5), (2, 4)]
```

**Why O(n):** We only loop through the list once. Each `in seen` lookup is
O(1) because sets are hash tables — they check membership in constant time
regardless of how many elements are in the set. No inner loop needed at all.

The trade-off: the set version uses extra O(n) memory. The nested loop version
uses O(1) extra memory. This is the classic time vs space trade-off.

---

### Q3: is_prime() Bug Analysis

```python
# Buggy version
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):     # Bug: should be range(2, int(n**0.5) + 1)
        if n % i == 0:
            return False
    return True
```

**The bug:** `range(2, n)` checks every number from 2 up to n-1. This works
correctly — it gives the right answer — but it is extremely slow. For n = 1,000,000
it does 999,998 divisions. This is O(n) time.

**Why range(2, sqrt(n)+1) is enough:**
If n has a factor greater than its square root, it must also have a corresponding
factor *smaller* than its square root. So if we haven't found any factor by the time
we reach sqrt(n), there are no factors at all — n is prime. This cuts the work from
O(n) to O(sqrt(n)), which is a massive improvement for large numbers.

**Fixed version:**

```python
def is_prime(n):
    """Check if n is prime. O(sqrt(n)) time."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:      # quick even-number shortcut
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):   # odd numbers only from 3
        if n % i == 0:
            return False
    return True
```

Two additional improvements:
1. Check for even numbers first (before the loop) and then only iterate odd
   numbers — this halves the number of iterations again.
2. Handle `n == 2` explicitly since it is the only even prime.

**Comparison for n = 1,000,000:**
- Buggy version: ~999,998 iterations
- Fixed version: ~500 iterations (sqrt(1,000,000) = 1,000, halved for odds)

---

## Part C — AI-Augmented Task: Diamond Pattern

**Exact prompt used:**
> "Write a Python program that prints a diamond pattern of asterisks. The user
> inputs the number of rows for the upper half. Include proper spacing and use
> nested loops only (no string multiplication tricks)."

**Critical evaluation of AI output:**

What it got right:
- Basic two-loop structure (one for upper half, one for lower)
- range() direction was correct — ascending for upper, descending for lower
- Core idea of printing spaces then stars per row was right

What it got wrong:
1. Used `print(" " * spaces + "*" * stars)` throughout — that IS string
   multiplication. The prompt explicitly banned it. My version uses inner
   `for` loops instead.
2. Off-by-one in star count for lower half: used `range(2*i)` instead of
   `range(2*i - 1)`, making each lower row one star too wide.
3. No input validation — n=0 or n=-3 caused silent incorrect output.
4. No mention of time complexity anywhere. This is O(n²) because for each
   of the ~2n rows we iterate up to n times in inner loops.
5. n=1 comment in the AI's code said "prints 3 rows" — actually prints 1.
   Wrong inline documentation.

My improved version (`diamond_pattern.py`) addresses all five issues.

---

## Part D — Transaction Analyzer (Bonus)

See `transaction_analyzer.py`. Demonstrates:
- `while` loop collecting transactions until `done`
- `break` to exit on done, `continue` to skip invalid inputs
- `for` loop with `enumerate` for the bar chart
- Dictionary for category spending breakdown
- High-value flag for transactions > Rs 10,000
