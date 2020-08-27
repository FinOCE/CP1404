TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")

tariff = int(input("Which tariff? 11 or 31: "))

while tariff != TARIFF_11 and tariff != TARIFF_31:
    if tariff == 31:
        tariff = TARIFF_31
    elif tariff == 11:
        tariff = TARIFF_11
    else:
        print("Invalid tariff")
        tariff = int(input("Which tariff? 11 or 31: "))

daily_use = float(input("Enter daily use in kWh: "))

while daily_use < 0:
    print("Invalid daily usage")
    daily_use = float(input("Enter daily use in kWh: "))

billing_days = float(input("Enter number of billing days: "))

while billing_days < 0:
    print("Invalid daily usage")
    billing_days = float(input("Enter number of billing days: "))

estimated_bill = billing_days * daily_use * tariff

print(f"Estimated bill: ${estimated_bill:.2f}")