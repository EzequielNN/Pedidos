from calendar import c
from tkinter import *
import tkinter
import sqlite3
from turtle import color


class Gui():

    window = Tk()
    window.wm_title("Pedidos")

    txtNumeropedido = StringVar
    txtCliente = StringVar
    txtEndereco = StringVar
    txtEntregador = StringVar
    txtFormapagamento = StringVar

    lblnumeropedido = Label(window, text=("Numero do pedido"))
    lblcliente = Label(window, text=("Nome do cliente"))
    lblendereco = Label(window, text=("Endereço do cliente"))
    lblentregador = Label(window, text=("Entregador responsavel"))
    lblformapagamento = Label(window, text=("Forma de pagamento"))

    entnumeropedido = Entry(window, textvariable=txtNumeropedido)
    entcliente = Entry(window, textvariable=txtCliente)
    entendereco = Entry(window, textvariable=txtEndereco)
    ententregador = Entry(window, textvariable=txtEntregador)
    entformapagamento = Entry(window, textvariable=txtFormapagamento)

    listClientes = Listbox(window)
    scrollClientes = Scrollbar(window)

    btnVertodos = Button(window, text="Ver Todos")
    btnBuscar = Button(window, text="Buscar pedido")
    btnInserir = Button(window, text="Inserir")
    btnUpdate = Button(window, text="Atualizar Selecionados")
    btnDel = Button(window, text="Deletar Selecionados")
    btnClose = Button(window, text="Fechar")

    lblnumeropedido.grid(row=0, column=0)
    lblcliente.grid(row=1, column=0)
    lblendereco.grid(row=2, column=0)
    lblentregador.grid(row=3, column=0)
    lblformapagamento.grid(row=4, column=0)
    entnumeropedido.grid(row=0, column=1)
    entcliente.grid(row=1, column=1)
    entendereco.grid(row=2, column=1)
    ententregador.grid(row=3, column=1)
    entformapagamento.grid(row=4, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnVertodos.grid(row=5, column=0, columnspan=2)
    btnBuscar.grid(row=6, column=0, columnspan=2)
    btnInserir.grid(row=7, column=0, columnspan=2)
    btnUpdate.grid(row=8, column=0, columnspan=2)
    btnDel.grid(row=9, column=0, columnspan=2)
    btnClose.grid(row=10, column=0, columnspan=2)

    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    x_pad = 5
    y_pad = 3
    width_entry = 30

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    def run(self):
        Gui.window.mainloop()
        
        
        
        