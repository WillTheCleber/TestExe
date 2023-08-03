#aqui é aonde vai acontecer a criação das tables do banco, só com nome

import pymysql

conn= pymysql.connect(db="banco",user="python", passwd="python123",host="localhost")

cursor = conn.cursor()

cursor.execute('''insert into cliente_poupanca(nome,cpf,contato)
                values ("Teste", "5555","contato")''')

conn.commit()

conn.close