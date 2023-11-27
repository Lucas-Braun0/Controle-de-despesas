import csv
from datetime import datetime
def pedir_valor_despesa():
    while True:
        try:
            valor = float(input("Valor da despesa em reais (R$): "))
            return valor
        except ValueError:
            print("Por favor, insira um número válido.")
def adicionar_despesa(despesas, arquivo):
    valor = pedir_valor_despesa()
    categoria = input("Categoria: ").upper()
    data = input("Data (DD/MM/YYYY): ")
    despesas.append({'valor': valor, 'categoria': categoria, 'data': data})
    with open(arquivo, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['valor', 'categoria', 'data'])
        writer.writerow({'valor': valor, 'categoria': categoria, 'data': data})
def listar_despesas(despesas):
    for despesa in despesas:
        print(f"{despesa['data']} - {despesa['categoria']}: {despesa['valor']}")
def total_gasto(despesas):
    return sum(despesa['valor'] for despesa in despesas)
def filtrar_por_categoria(despesas, categoria):
    return [despesa for despesa in despesas if despesa['categoria'] == categoria]
# Inicialização e leitura do arquivo
arquivo_despesas = 'despesas.csv'
despesas = []
try:
    with open(arquivo_despesas, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['valor'] = float(row['valor'])
            despesas.append(row)
except FileNotFoundError:
    with open(arquivo_despesas, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['valor', 'categoria', 'data'])
        writer.writeheader()
# Interface do usuário.
while True:
    print("\nOrganizador de Despesas Pessoais")
    print("1. Adicionar despesa")
    print("2. Listar todas as despesas")
    print("3. Total gasto")
    print("4. Filtrar por categoria")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        adicionar_despesa(despesas, arquivo_despesas)
    elif opcao == '2':
        listar_despesas(despesas)
    elif opcao == '3':
        total = total_gasto(despesas)
        print(f"Total gasto: {total}")
    elif opcao == '4':
        categoria = input("Digite a categoria: ").upper()
        filtradas = filtrar_por_categoria(despesas, categoria)
        listar_despesas(filtradas)
    elif opcao == '5':
        break
    else:
        print("Opção inválida!")
