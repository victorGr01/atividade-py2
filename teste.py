def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

print("=== CONVERSOR DE TEMPERATURA ===")
print("1 - Celsius → Fahrenheit")
print("2 - Fahrenheit → Celsius")

op = input("Escolha uma opção: ")

if op == "1":
    c = float(input("Digite a temperatura em °C: "))
    f = celsius_para_fahrenheit(c)
    print(f"{c}°C = {f:.2f}°F")

elif op == "2":
    f = float(input("Digite a temperatura em °F: "))
    c = fahrenheit_para_celsius(f)
    print(f"{f}°F = {c:.2f}°C")

else:
    print("Opção inválida!")
