# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento

def salario(vi):
    s = vi+(vi*0.15)
    print(f"{s:.2f}")
    
valor= float(input("Digite o valor do produto:"))    
salario(valor)