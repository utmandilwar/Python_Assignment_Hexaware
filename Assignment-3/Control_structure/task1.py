def check_eligibility(credit_score, annual_income):
    if credit_score > 700 and annual_income >= 50000:
        return True
    else:
        return False

credit_score = int(input("Enter the customer's credit score: "))
annual_income = int(input("Enter the customer's annual income: "))

eligibility = check_eligibility(credit_score, annual_income)

if eligibility:
    print("The customer is eligible for a loan.")
else:
    print("The customer is not eligible for a loan.")