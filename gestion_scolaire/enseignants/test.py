from datetime import date

ANNEES = []

for n in range(5):
    year = date.today().year + n - 3
    ANNEES.append(f'{year}{" - "}{year + 1}')

print(tuple(ANNEES))
