balance = 320000
annualInterestRate = 0.2

denom = 1
for i in range(12):
    denom *= (1 + annualInterestRate / 12)
    denom += 1
denom -= 1
ans = (balance * (1 + annualInterestRate / 12) ** 12) / denom
print(round(ans, 2))