# Calculates principal and interest on initial 1000 USD at 5% interest
# compounding annualy

balance = 1000

for year in range(5):
    balance *= 1.05

print(f'{balance:.2f}')