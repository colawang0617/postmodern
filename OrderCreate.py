import sys
from src.database.PasswordMatcher import PasswordMatcher

matcher = PasswordMatcher()
if len(sys.argv) < 2:
    print("Please enter the delivered item as the argument when running the program")
else:
    matcher.add_new_order(sys.argv[1])
    print("Successfully added the item")
