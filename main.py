from controller.order_controller import criar_pedido_seguro, criar_pedido_inseguro
from view.form import abrir_formulario


def main():
    print("1 - Inserir pedido (seguro)")
    print("2 - Inserir pedido (inseguro - simula SQL Injection)")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        abrir_formulario(criar_pedido_seguro)
    elif opcao == '2':
        abrir_formulario(criar_pedido_inseguro)
    else:
        print("Opção inválida.")
    

if __name__ == "__main__":
    main()
