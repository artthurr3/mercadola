supermercado = []

def adicionar_item(item):
    supermercado.append(item)
    print(f"{item} adicionado ao supermercado.")

def remover_item(item):
    if item in supermercado:
        supermercado.remove(item)
        print(f"{item} removido do supermercado.")
    else:
        print(f"{item} não encontrado no supermercado.")

def ver_itens():
    if supermercado:
        print("Itens no supermercado:")
        for item in supermercado:
            print("-", item)
def modificar_item(item_antigo, item_novo):
    if item_antigo in supermercado:
        index = supermercado.index(item_antigo)
        supermercado[index] = item_novo
        print(f"{item_antigo} modificado para {item_novo}.")
    
    else:
        print("O supermercado está vazio.")

def menu():
    while True:
        print("\n--- Supermercado ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Ver itens")
        print("4. Modificar item")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            item = input("Digite o nome do item para adicionar: ")
            adicionar_item(item)
        elif escolha == "2":
            item = input("Digite o nome do item para remover: ")
            remover_item(item)
        elif escolha == "3":
            ver_itens()
        elif escolha == "4":
            item_antigo = input("Digite o nome do item a ser modificado: ")
            item_novo = input("Digite o novo nome do item: ")
            modificar_item(item_antigo, item_novo)
        elif escolha == "5":
            sair()
        else:
            print("Opção inválida. Tente novamente.")

menu()