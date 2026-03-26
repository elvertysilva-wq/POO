expressao = input("Digite dois valores inteiros separados por um operador (+, -, * ou /): ")


for op in ['+', '-', '*', '/']:
    if op in expressao:
        operador = op
        break


num1, num2 = expressao.split(operador)


num1 = int(num1)
num2 = int(num2)


if operador == '+':
    resultado = num1 + num2
elif operador == '-':
    resultado = num1 - num2
elif operador == '*':
    resultado = num1 * num2
elif operador == '/':
    resultado = num1 / num2

print("O resultado da operação é", resultado)