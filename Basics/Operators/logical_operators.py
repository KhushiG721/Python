"""
Demonstrates Python logical operators.

Logical operators are used to combine Boolean expressions.
"""

has_ticket = True
has_valid_id = True
is_event_full = False


# --------------------------------------------------
# 1. AND
# --------------------------------------------------

can_enter = has_ticket and has_valid_id

print("AND:")
print("Can Enter:", can_enter)


# --------------------------------------------------
# 2. OR
# --------------------------------------------------

has_email_confirmation = False
has_sms_confirmation = True

is_confirmed = has_email_confirmation or has_sms_confirmation

print("\nOR:")
print("Registration Confirmed:", is_confirmed)


# --------------------------------------------------
# 3. NOT
# --------------------------------------------------

print("\nNOT:")
print("Event is Full:", is_event_full)
print("Event is Not Full:", not is_event_full)


# --------------------------------------------------
# 4. Combining Conditions
# --------------------------------------------------

can_register = has_valid_id and not is_event_full

print("\nCombined Conditions:")
print("Can Register:", can_register)