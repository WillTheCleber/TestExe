from classe_pai import dadosCliente
from classe_credito import clienteCredito
from comandos_funcoes import metodos
import pymysql

# conn= pymysql.connect(db="dbpython",user="python",passwd="python123",host="localhost")

#Aqui vou começar a brincar criando um menu para a pessoa poder interagir

t= True
while t == True:
    #descrição comandos
    print("""1- Cadastrar cliente
          2- Realizar Deposito
          3- Realizar Saque
          4-""")
    try:
        opcao= int(input("Selecione uma das opções: "))

        if opcao == 1:
            #MENU DENTRO DO MENU (Perguntando se a conta sera de credito)
            print("A conta sera poupança??")
            subopcao=bool(input("Aperte enter para confirmar. "))

            #CADASTRANDO CONTA POUPANÇA
            if subopcao==False:
                metodos.CadCliente()



            #CADASTRANDO CONTA CREDITO  
            elif subopcao == True:
                metodos.CadClienteCredito()
                

            else:
                print("Erro na seleção de cliente.")


    #EXCEPTS ATUAIS, perguntar se mais vale o try estar em cada função----
    except TypeError:
        print("Valor Digitado invalido, refaça a operação.")            
    except:
        print("Erro inesperado.")




