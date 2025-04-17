import tkinter as tk
from tkinter import messagebox, ttk

def abrir_formulario(controller):
    def enviar_pedido():
        dados = {
            "customer_name": entry_cliente.get(),
            "employee_name": entry_vendedor.get(),
            "order_date": entry_data.get()
        }
        sucesso, resultado = controller.criar_pedido(dados)
        if sucesso:
            messagebox.showinfo("Sucesso", f"Pedido {resultado} inserido com sucesso!")
            entry_id_pedido_produto.insert(0, resultado)
            entry_id_pedido_rel1.insert(0, resultado)
        else:
            messagebox.showerror("Erro", "Falha ao inserir pedido:\n" + str(resultado))

    def inserir_produto():
        dados = {
            "order_id": entry_id_pedido_produto.get(),
            "product_id": entry_produto.get(),
            "quantity": entry_qtd.get(),
            "unit_price": entry_preco.get(),
            "discount": entry_desc.get()
        }
        sucesso, msg = controller.inserir_produto(dados)
        if sucesso:
            messagebox.showinfo("Sucesso", "Produto inserido no pedido com sucesso!")
        else:
            messagebox.showerror("Erro", "Erro ao inserir produto:\n" + str(msg))

    def gerar_relatorio1():
        dados = {
            "order_id": entry_id_pedido_rel1.get(),
        }
        resultado = controller.gerar_relatorio_order(dados)
        messagebox.showinfo("Relatório 1", resultado)

    def gerar_relatorio2():
        dados = {
            "date_start": entry_data_inicio.get(),
            "date_end": entry_data_fim.get(),
        }
        resultado = controller.gerar_relatorio_employee(dados)
        messagebox.showinfo("Relatório 2", resultado)

    janela = tk.Tk()
    janela.title("João Henrique Flauzino (2023001577) e Beatriz Nascimento (2023007113)")
    janela.geometry("800x400")

    quadro1 = tk.LabelFrame(janela, text="Pedido", padx=10, pady=10)
    quadro1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    tk.Label(quadro1, text="Nome do Cliente").grid(row=0, column=0)
    entry_cliente = tk.Entry(quadro1)
    entry_cliente.grid(row=0, column=1)

    tk.Label(quadro1, text="Nome do Empregado").grid(row=1, column=0)
    entry_vendedor = tk.Entry(quadro1)
    entry_vendedor.grid(row=1, column=1)

    tk.Label(quadro1, text="Data (YYYY-MM-DD)").grid(row=2, column=0)
    entry_data = tk.Entry(quadro1)
    entry_data.grid(row=2, column=1)

    btn_pedido = tk.Button(quadro1, text="Inserir Pedido", command=enviar_pedido)
    btn_pedido.grid(row=3, columnspan=2, pady=10)

    quadro2 = tk.LabelFrame(janela, text="Produto no Pedido", padx=10, pady=10)
    quadro2.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    tk.Label(quadro2, text="ID do Produto").grid(row=0, column=0)
    entry_produto = tk.Entry(quadro2)
    entry_produto.grid(row=0, column=1)

    tk.Label(quadro2, text="ID do Pedido").grid(row=1, column=0)
    entry_id_pedido_produto = tk.Entry(quadro2)
    entry_id_pedido_produto.grid(row=1, column=1)

    tk.Label(quadro2, text="Quantidade").grid(row=2, column=0)
    entry_qtd = tk.Entry(quadro2)
    entry_qtd.grid(row=2, column=1)

    tk.Label(quadro2, text="Preço por Unidade").grid(row=3, column=0)
    entry_preco = tk.Entry(quadro2)
    entry_preco.grid(row=3, column=1)

    tk.Label(quadro2, text="Desconto").grid(row=4, column=0)
    entry_desc = tk.Entry(quadro2)
    entry_desc.grid(row=4, column=1)

    btn_produto = tk.Button(quadro2, text="Inserir Produto no Pedido", command=inserir_produto)
    btn_produto.grid(row=5, columnspan=2, pady=10)

    quadro3 = tk.LabelFrame(janela, text="Relatório por Pedido", padx=10, pady=10)
    quadro3.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    tk.Label(quadro3, text="ID do Pedido").grid(row=0, column=0)
    entry_id_pedido_rel1 = tk.Entry(quadro3)
    entry_id_pedido_rel1.grid(row=0, column=1)

    btn_relatorio1 = tk.Button(quadro3, text="Relatório 1", command=gerar_relatorio1)
    btn_relatorio1.grid(row=1, columnspan=2, pady=10)

    quadro4 = tk.LabelFrame(janela, text="Relatório por Período", padx=10, pady=10)
    quadro4.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

    tk.Label(quadro4, text="Data Começo").grid(row=0, column=0)
    entry_data_inicio = tk.Entry(quadro4)
    entry_data_inicio.grid(row=0, column=1)

    tk.Label(quadro4, text="Data Final").grid(row=1, column=0)
    entry_data_fim = tk.Entry(quadro4)
    entry_data_fim.grid(row=1, column=1)

    btn_relatorio2 = tk.Button(quadro4, text="Relatório 2", command=gerar_relatorio2)
    btn_relatorio2.grid(row=2, columnspan=2, pady=10)

    janela.mainloop()
