#https://www.beecrowd.com.br/judge/pt/problems/view/1009
vendedor = input()
salario = float(input())
vendas = float(input())

total = salario + 0.15 * vendas

print(f"TOTAL = R$ {total:.2f}")