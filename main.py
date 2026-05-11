clients = [
    {"name": "Ali", "money": 1200},
    {"name": "Vali", "money": 540},
    {"name": "Sami", "money": 3400},
    {"name": "Aziza", "money": 900}
]

rich = []
normal = []

for client in clients:
    if client["money"] >= 1000:
        rich.append(client["name"])
    else:
        normal.append(client["name"])

print("Boy mijozlar:")

for item in rich:
    print(item)

print("Oddiy mijozlar:")

for item in normal:
    print(item)

total = 0

for client in clients:
    total += client["money"]

print("Bankdagi jami pul:", total)
