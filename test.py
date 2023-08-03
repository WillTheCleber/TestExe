from classe_pai import dadosCliente
from classe_credito import clienteCredito
from comandos_funcoes import CadCliente, CadClienteCredito
import pymysql

conn= pymysql.connect(db="dbpython",user="python",passwd="python123",host="localhost")

opcao= int(input("Selecione uma das opções: "))

if opcao == 1:
            #MENU DENTRO DO MENU (Perguntando se a conta sera de credito)
            print("A conta sera poupança??")
            subopcao=bool(input("Aperte enter para confirmar. "))

            #CADASTRANDO CONTA POUPANÇA
            if subopcao==False:
                CadCliente()



            #CADASTRANDO CONTA CREDITO  
            elif subopcao == True:
                CadClienteCredito()
                

            else:
                print("Erro na seleção de cliente.")