# Receba um numero e exiba se ele é positivo ou negativo

numero = float(input("Digite um numero para verificar se é positivo ou negativo: "))

if numero < 0:
  print("numero negativo")

elif numero > 0:
  print("numero positivo")

else: 
  print("numero neutro")


# Receba uma temperatura em farenheit e exiba em graus celsius.

temperatura_fahrenheit = int(input("Digite a temperatura: "))

temperatura_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)

print(f"Convertida ficou em: {temperatura_celsius:.2f}°C")
