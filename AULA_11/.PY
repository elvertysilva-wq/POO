from datetime import datetime

x = datetime(2026, 5, 19, 15, 30, 10)
print(x)
print(type(x))
y = datetime(2000, 1, 5)

print(x.day)
print(x.month)
print(x.year)
print(x.hour)
print(x.second)
print(x.microsecond)

z = datetime.now(Zoneinfo("America/Sao_Paulo"))
print(z)