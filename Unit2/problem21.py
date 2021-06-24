def balCalc(balance, annualInterestRate, monthlyPaymentRate):
    for i in range(12):
        balance -= monthlyPaymentRate * balance
        balance *= 1 + annualInterestRate / 12
    return round(balance, 2)

def balCalcRec(balance, annualInterestRate, monthlyPaymentRate, months = 12):
        if months == 1:
            return balance * (1 - monthlyPaymentRate) * (1 + annualInterestRate / 12)
        else:
            if months == 12:
                return round(balCalcRec(balance, annualInterestRate, monthlyPaymentRate, months - 1) * (1 - monthlyPaymentRate) * (1 + annualInterestRate / 12), 2)
            else:
                return balCalcRec(balance, annualInterestRate, monthlyPaymentRate, months - 1) * (1 - monthlyPaymentRate) * (1 + annualInterestRate / 12)