balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance -= monthlyPaymentRate * balance
    balance *= 1 + annualInterestRate / 12

print(round(balance, 2))