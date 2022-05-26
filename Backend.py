from http import client
import sqlite3 as sql


class TransactionObject():
    database    = "clientes.db"
    conn        = None
    cur         = None
    connected   = False
 
    def connect(self):
        TransactionObject.conn      = sql.connect(TransactionObject.database)
        TransactionObject.cur       = TransactionObject.conn.cursor()
        TransactionObject.connected = True
 
    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False
 
    def execute(self, sql, parms = None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False
 
    def fetchall(self):
        return TransactionObject.cur.fetchall()
 
    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False


def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS Pedidos (id INTEGER PRIMARY KEY , Numero pedido TEXT, Cliente TEXT, Endereço TEXT, Entregador TEXT, Forma de pagamento TEXT)")
    trans.persist()
    trans.disconnect()
 
initDB()

def view():
    trans = TransactionObject()
    trans.connect()
 
    trans.execute("SELECT * FROM Pedidos")
 
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def insert(Numero_do_pedido, Cliente, Endereço, Entregador, Forma_de_Pagamento):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO Pedidos VALUES(NULL, ?,?,?,?,?)", (Numero_do_pedido, Cliente, Endereço, Entregador, Forma_de_Pagamento))
    trans.persist()
    trans.disconnect()

def search(Numero_do_pedido="", Cliente="", Endereço="", Entregador="", Forma_de_Pagamento=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM Pedidos WHERE Numero_do_pedido=? or Cliente=? or Endereço=? or Entregador=? or Forma_de_Pagamento=?", (Numero_do_pedido, Cliente, Endereço, Entregador, Forma_de_Pagamento))
    rows = trans.fetchall()
    trans.disconnect()
    return rows

def update(id, Numero_do_pedido, Cliente, Endereço, Entregador, Forma_de_Pagamento):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE Pedidos SET Numero_do_pedido =?, Cliente=?, Endereço=?, Entregador=?, Forma_de_Pagamento=? WHERE id = ?",(Numero_do_pedido, Cliente, Endereço, Entregador, Forma_de_Pagamento, id))
    trans.persist()
    trans.disconnect()


def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM Pedidos WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()















