import tkinter as tk
from tkinter import messagebox

def abrir_formulario(controller):
    def enviar():
        dados = {
            "customer_name": entry_cliente.get(),
            "employee_name": entry_vendedor.get(),
            "order_date": entry_data.get(),
            "product_id": entry_produto.get(),
            "quantity": entry_qtd.get()
        }
        sucesso, erro = controller.criar_pedido(dados)
        if sucesso:
            messagebox.showinfo("Sucesso", "Pedido inserido com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao inserir pedido:\n" + str(erro))
    def relatorio():
        relatorio_result = controller.relatorio()
        tk.Label(janela, text=relatorio_result).grid(row=7, column=0,columnspan=2)
        

    janela = tk.Tk()
    janela.title("Cadastro de Pedido")

    tk.Label(janela, text="Nome Cliente").grid(row=0, column=0)
    entry_cliente = tk.Entry(janela)
    entry_cliente.grid(row=0, column=1)

    tk.Label(janela, text="Nome Vendedor").grid(row=1, column=0)
    entry_vendedor = tk.Entry(janela)
    entry_vendedor.grid(row=1, column=1)

    tk.Label(janela, text="Data (YYYY-MM-DD)").grid(row=2, column=0)
    entry_data = tk.Entry(janela)
    entry_data.grid(row=2, column=1)

    tk.Label(janela, text="ID Produto").grid(row=3, column=0)
    entry_produto = tk.Entry(janela)
    entry_produto.grid(row=3, column=1)

    tk.Label(janela, text="Quantidade").grid(row=4, column=0)
    entry_qtd = tk.Entry(janela)
    entry_qtd.grid(row=4, column=1)

    btn = tk.Button(janela, text="Enviar Pedido", command=enviar)
    btn.grid(row=5, columnspan=2, pady=10)

    btn = tk.Button(janela, text="Gerar Relatório", command=relatorio)
    btn.grid(row=6, columnspan=2, pady=10)

    janela.mainloop()
