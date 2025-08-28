print("Welcome to the tip calculator")

BILL = float(input("What is your total bill?"))
TIP = int(input("What is your tip percentage?"))
PEOPLE = int(input("How many people are splitting the bill?"))
TIP_AS_PERCENT = TIP / 100
TOTAL_TIP_AMOUNT = BILL * TIP_AS_PERCENT
TOTAL_BILL = BILL + TOTAL_TIP_AMOUNT
SPLIT_BILL = TOTAL_BILL / PEOPLE
print(f"Each person must pay {round(SPLIT_BILL, 2)}")
