from view.form import coletar_dados_pedido
from dao.order_dao import inserir_pedido

def criar_pedido():
    dados = coletar_dados_pedido()

    sucesso = inserir_pedido(
        customer_id=dados["customer_id"],
        employee_id=dados["employee_id"],
        order_date=dados["order_date"],
        product_id=dados["product_id"],
        quantity=dados["quantity"]
    )

    if sucesso:
        print("\nPedido inserido com sucesso")
    else:
        print("\nFalha ao inserir pedido")
