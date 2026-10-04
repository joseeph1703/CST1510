"""
RECORD CHECK  -  my version
===========================

<<<<<<< HEAD
Name  :joseph Muyumba Kalala
Lane  :  AI   
Date  :11-03-2026
=======
Name  : Joseph Muyumba Kalala
Lane  :  AI     
Date  :10-03-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
#<<<<<< HEAD
# 1. Ask the user for your three values.
#=====
# 1. Ask for your three values.
#>>>>>>> 53ff3baa718066af74a770e6d3cc55b939983e13
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#<<<<<<< HEAD
#
#    Remember: input() always gives back text.

label = input("Label: ")
first = float(input("First number: "))
second = float(input("Second number: "))



# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = first - second
percent = (first / second) * 100


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print(f"Label       : {label}")
print(f"First value : {first:>10.2f}")
print(f"Second value: {second:>10.2f}")
print(f"Difference  : {difference:+10.2f}")
print(f"Percent     : {percent:>10.2f} %")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you

label = input("Enter label (text): ")
value = float(input("Enter value (number): "))
limit = float(input("Enter limit (number): "))
# ================================================================== PROCESS
# 2. Work out the difference and the percentage.       [Typical and above]

difference = value - limit
percent = (value / limit) * 100
# 3. Decide a status and store it in a variable called status.
#
#    Threshold : if / else        -> "OVER LIMIT" or "OK"
#    Typical   : if / elif / else -> "OVER LIMIT" (100% or more),
#                                     "WARNING" (90% or more), otherwise "OK"

#status = ""   # replace with your if / else (or if / elif / else)
if percent >= 100:
    status = "OVER LIMIT"
elif percent >= 90:
    status = "WARNING"
else:
    status = "OK"

# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : wrap sections 1-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# your report lines go here

print("=" * 34)
print(f" RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Value:       {value}")
print(f"Limit:       {limit}")
print(f"Difference:  {difference}")
print(f"Percent:     {percent:>6.2f}%")
print(f"Status:      {status}")

print("=" * 34)



# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every variable name says what it holds
#>>>>>> 53ff3baa718066af74a770e6d3cc55b939983e13
