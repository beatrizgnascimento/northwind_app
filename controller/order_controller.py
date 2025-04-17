from dao.order_dao import inserir_pedido_seguro, inserir_pedido_inseguro

def criar_pedido_seguro(dados):
    return inserir_pedido_seguro(
        customer_id=dados["customer_id"],
        employee_id=dados["employee_id"],
        order_date=dados["order_date"],
        product_id=dados["product_id"],
        quantity=dados["quantity"]
    )

def criar_pedido_inseguro(dados):
    return inserir_pedido_inseguro(
        customer_id=dados["customer_id"],
        employee_id=dados["employee_id"],
        order_date=dados["order_date"],
        product_id=dados["product_id"],
        quantity=dados["quantity"]
    )
