m = int(input())
print(m)

note100 = m // 100
print(f"{note100} nota(s) de R$ 100,00")
m %= 100

note50 = m // 50
print(f"{note50} nota(s) de R$ 50,00")
m %= 50

note20 = m // 20
print(f"{note20} nota(s) de R$ 20,00")
m %= 20

note10 = m // 10
print(f"{note10} nota(s) de R$ 10,00")
m %= 10

note5 = m // 5
print(f"{note5} nota(s) de R$ 5,00")
m %= 5

note2 = m // 2
print(f"{note2} nota(s) de R$ 2,00")
m %= 2

print(f"{m} nota(s) de R$ 1,00")