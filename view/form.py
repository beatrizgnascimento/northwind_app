import tkinter as tk
from tkinter import messagebox

def abrir_formulario(controller_funcao):
    def enviar():
        dados = {
            "customer_id": entry_cliente.get(),
            "employee_id": entry_vendedor.get(),
            "order_date": entry_data.get(),
            "product_id": entry_produto.get(),
            "quantity": entry_qtd.get()
        }
        sucesso = controller_funcao(dados)
        if sucesso:
            messagebox.showinfo("Sucesso", "Pedido inserido com sucesso!")
        else:
            messagebox.showerror("Erro", "Falha ao inserir pedido.")

    janela = tk.Tk()
    janela.title("Cadastro de Pedido")

    tk.Label(janela, text="ID Cliente").grid(row=0, column=0)
    entry_cliente = tk.Entry(janela)
    entry_cliente.grid(row=0, column=1)

    tk.Label(janela, text="ID Vendedor").grid(row=1, column=0)
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

    janela.mainloop()
