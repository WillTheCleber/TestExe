from classe_pai import dadosCliente
from classe_credito import clienteCredito
from comandos_funcoes import CadCliente, CadClienteCredito
import pymysql

conn= pymysql.connect(db="dbpython",user="python",passwd="python123",host="localhost")

opcao= int(input("Selecione uma das opções: "))

if opcao == 1:
            #MENU DENTRO DO MENU (Perguntando se a conta sera de credito)
            print("O conta será de credito?")
            subopcao=bool(input("Aperte apenas enter para negar. "))

            #CADASTRANDO CONTA POUPANÇA
            if subopcao==False:
                CadCliente()



            #CADASTRANDO CONTA CREDITO  
            elif subopcao == True:
                CadClienteCredito()
                

            else:
                print("Erro na seleção de cliente.")