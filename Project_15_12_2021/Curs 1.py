"""
Test bank account exercise
"""
expected_user: str = "Oana"
expected_pwd: str = "123abc"
expected_sold: int = 100

# Implement the first test case
usr = input("Please enter a valid username:")
assert usr == expected_user
print(type(expected_sold))

pwd = input("Please enter a valid password:")
assert pwd == expected_pwd

input("Please enter to login")
print(f"Login successful! Your sold is:{expected_sold}")

cashback = int( input("Please enter the amount you want to retrieve:"))
print(f"You have {expected_sold - cashback} euro left in your account")





