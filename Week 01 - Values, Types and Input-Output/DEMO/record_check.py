"""
<<<<<<< HEAD
RECORD CHECK  -  Week 1 version
===============================
Run it with:    python record_check.py

This is a demonstration program, not your coursework. You will see it again
each week, doing the same job a bit better, as you learn new tools:

    Week 1   input, calculate, print          <- this version
    Week 2   it can make decisions
=======
RECORD CHECK  -  Week 2 version
================================
Run it with:    python record_check.py

    Week 1   input, calculate, print
    Week 2   it can make decisions          <- this version
>>>>>>> 53ff3baa718066af74a770e6d3cc55b939983e13
    Week 3   it is built from functions
    Week 4   it reads many records from a file
    Week 5   it becomes a reusable component
    Week 6   it does the whole job in a few lines

<<<<<<< HEAD
The point is not the program. The point is watching the SAME problem get
easier as your toolkit grows.

In today's lab you build your own small version of the two boxes below.
That is finished in the lab - nothing carries over to next week.

You are not expected to understand every line today. Two lines use ideas
from Week 2 and they are marked.
"""

# ------------------------------------------------------------------ INPUT
record_id = input("Record ID : ")
value     = float(input("Value     : "))
limit     = float(input("Limit     : "))

# ------------------------------------------------------------------ STORE
# Week 4. For now, one record lives in three variables.

# ---------------------------------------------------------------- PROCESS
difference = value - limit
percent    = (value / limit) * 100

status = "OVER LIMIT" if difference > 0 else "OK"   # <- Week 2

# ----------------------------------------------------------------- OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {record_id}")
print("=" * 34)
print(f"  Value       : {value:>10.2f}")
print(f"  Limit       : {limit:>10.2f}")
print(f"  Difference  : {difference:>+10.2f}")
print(f"  Of limit    : {percent:>9.1f} %")
print(f"  Status      : {status:>10}")
print("=" * 34)
#=======
while True:
    # --------------------------------------------------------------- INPUT
    record_id = input("Record ID (or 'quit') : ")
    if record_id == "quit":
        break

    value = float(input("Value    : "))
    limit = float(input("Limit    : "))

    # --------------------------------------------------------------- STORE
    # Week 4. For now, one record still lives in three variables.

    # --------------------------------------------------------------- PROCESS
    difference = value - limit
    percent = (value / limit) * 100     # <- Week 3 will pull this out into a function

    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    # --------------------------------------------------------------- OUTPUT
    print()
    print("-" * 34)
    print(f" RECORD CHECK  - {record_id}")
    print("-" * 34)
    print(f" Value         : {value:>10.2f}")
    print(f" Limit         : {limit:>10.2f}")
    print(f" Difference    : {difference:>10.2f}")
    print(f" Of limit      : {percent:>9.1f} %")
    print(f" Status        : {status:>10}")
    print("-" * 34)
    print()
    print("Done. Checked and reported.")
