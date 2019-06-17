from Musica import Musica
from Node import Node
from musica_mock import create_mock

def menu():
    print("="*30)
    print("1- Inserir uma música")
    print("2- Procurar uma música pelo nome")
    print("3- Procurar todas as músicas de um determinado ano")
    print("4- Remover uma música pelo nome")
    print("5- Listar todas as músicas")
    print("6- Saber a altura da arvore")
    print("7- Esta balanceada? ")
    print("8- Sair")
    print("="*30)
    choice = int(input("Option: "))
    return choice

def create_musica_and_insert(root):
    nome = input("Nome da musica: ")
    autor = input("Nome do autor: ")
    album = input("Nome do album: ")
    ano = int(input("Ano de lançamento: "))
    musica = Musica(nome=nome, autor=autor, album=album, ano=ano)
    root = root.insert(musica)
    return root

def search(root, nome):
    result = root.search_by_name(nome)
    if result is not None:
        print(result.get_nome())
        print(result.get_ano())
        print(result.get_autor())
        print(result.get_album())
    else:
        print("Musica nao encontrada")


def main():
    load = input("Carregar o mock? (s/n)")
    if load == "s":
        #arvore mockada
        root = create_mock()
    else:
        #arvore vazia
        root = Node()
    print(root.get_left().balance)
    
    root.list_items()
    print(root.is_balanced(root))
    exit()
    choice = menu()
    while choice != 8:
        if  choice == 1:
            root  = create_musica_and_insert(root)
        elif choice == 2:
            nome = input("Nome da musica: ")
            search(root, nome)
        elif choice == 3:
            ano = int(input("Ano: "))
            root.search_by_year(ano)
        elif choice == 4:
            nome = input("Nome da musica que deseja remover: ")
            root.remove_by_name(nome)
        elif choice == 5:
            print("Lista de todas as musicas: ")
            root.list_items()
        elif choice == 6:
            print("Altura da arvore: ", root.height(root) - 1)
        elif choice == 7:
            result = root.is_balanced(root)
            if result == True:
                print("Arvore balanceada")
            else:
                print("Arvore nao esta balanceada")
        choice = menu()
if __name__ == "__main__":
    main()
