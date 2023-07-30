#aqui é aonde vai acontecer a criação das tables do banco, só com nome

import pymysql

conn= pymysql.connect(db="banco",user="python", passwd="python123",host="localhost")

cursor = conn.cursor()

cursor.execute('''create table cadastro_clientes(
id integer not null primary key auto_increment,
nome varchar(100) not null,
sobrenome varchar(100) not null,
cpf varchar(11),
conta int
)''')

# conn.commit()

conn.close