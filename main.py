from controller.order_controller import Controller
from dao.dao_seguro import DAOSeguro
from dao.dao_inseguro import DAOInseguro
from dao.dao_orm import DAOOrm
from db_config import get_connection, get_engine
from view.form import abrir_formulario


def main():
    print("1 - Inserir pedido (seguro)")
    print("2 - Inserir pedido (inseguro - simula SQL Injection)")
    print("3 - Inserir pedido (ORM)")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        abrir_formulario(Controller(DAOSeguro(get_connection,get_engine)))
    elif opcao == '2':
        abrir_formulario(Controller(DAOInseguro(get_connection,get_engine)))
    elif opcao == '3':
        abrir_formulario(Controller(DAOOrm(get_connection,get_engine)))
    else:
        print("Opção inválida.")
    

if __name__ == "__main__":
    main()
