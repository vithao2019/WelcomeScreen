riscos = []

while True:

    risco = input("Novo risco (fim para sair): ")

    if risco == "fim":
        break

    riscos.append(risco)

print("\nRAID LOG")

for item in riscos:
    print(f"- {item}")