from Pedidos import *
import Backend as core

app = Gui()




def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)


def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNumeropedido.get(), app.txtCliente.get(
    ), app.txtEndereco.get(), app.txtEntregador.get(), app.txtFormapagamento.get())
    for r in rows:
        app.listClientes.insert(END, r)


def insert_command():
    core.insert(app.txtNumeropedido.get(), app.txtCliente.get(
    ), app.txtEndereco.get(), app.txtEntregador.get(), app.txtFormapagamento.get())
    view_command()


def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entnumeropedido.delete(0, END)
    app.entnumeropedido.insert(END, selected[1])
    app.entcliente.delete(0, END)
    app.entcliente.insert(END, selected[2])
    app.entendereco.delete(0, END)
    app.entendereco.insert(END, selected[3])
    app.ententregador.delete(0, END)
    app.ententregador.insert(END, selected[4])
    app.entformapagamento.delete(0, END)
    app.entformapagamento.insert(END, selected[5])


app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)


def update_command():
    core.update(selected[0], app.txtNumeropedido.get(), app.txtCliente.get(
    ), app.txtEndereco.get(), app.txtEntregador.get(), app.txtFormapagamento.get())
    view_command()


def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

app.btnVertodos.configure(command=view_command)
app.btnBuscar.configure(command=search_command)
app.btnInserir.configure(command=insert_command)
app.btnUpdate.configure(command=update_command)
app.btnDel.configure(command=del_command)
app.btnClose.configure(command=app.window.destroy)

app.run()
