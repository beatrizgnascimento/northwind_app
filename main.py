from controller.order_controller import criar_pedido_seguro, criar_pedido_inseguro, criar_pedido_orm
from view.form import abrir_formulario


def main():
    print("1 - Inserir pedido (seguro)")
    print("2 - Inserir pedido (inseguro - simula SQL Injection)")
    print("3 - Inserir pedido (ORM)")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        abrir_formulario(criar_pedido_seguro)
    elif opcao == '2':
        abrir_formulario(criar_pedido_inseguro)
    elif opcao == '3':
        abrir_formulario(criar_pedido_orm)
    else:
        print("Opção inválida.")
    

if __name__ == "__main__":
    main()
