def coletar_dados_pedido():
    print("=== Novo Pedido ===")

    customer_id = input("ID do cliente: ")
    employee_id = input("ID do vendedor: ")
    order_date = input("Data do pedido (YYYY-MM-DD): ")
    product_id = input("ID do produto: ")
    quantity = input("Quantidade: ")

    input("Pressione Enter para continuar")

    return {
        "customer_id": customer_id,
        "employee_id": employee_id,
        "order_date": order_date,
        "product_id": product_id,
        "quantity": quantity
    }
