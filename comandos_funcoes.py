from classe_credito import clienteCredito
from classe_pai import dadosCliente
import pymysql
import time


#FUNÇÃO CADASTRO CLIENTE POUPANÇA

#Aqui registrei as funções que irão para meu programa principal(main), aonde recolho os dados necessario para registrar o cliente e depois peço uma verificação manual
#apos a confirmação chamo o cursor e do insert no BD com um aviso no programa falando que foi registrado.
class metodos(dadosCliente):
        
    def CadCliente(self):
        #BLOCO 1

        #recolhendo dados para cadastrar cliente
        nomeCadastro= input("Digite o nome do cliente: ")
        cpfCadastro= input("Digite o CPF do cliente: ")
        contatoCadastro= input("Digite o contato do cliente: ") #Variaveis input

        #BLOCO 2 (ERRO: EXIBINDO %s)
        print("""Confirmação de registro:
        Nome: %s
        CPF: %s
        Contato: %s
        Aperte enter para confirmar.""",(nomeCadastro,cpfCadastro,contatoCadastro)) #Exibindo os atributos para ser confirmado


        #CONFIRMAÇÃO
        confirma= bool(input(''))


        #BLOCO 3 (ERRO: Entra no true e ja vai para a parte do exception)
        if confirma== False:



            #Criação do objeto e atribuindo os mesmos
            cadastro=dadosCliente()
            cadastro.nome= nomeCadastro
            cadastro.cpf= cpfCadastro
            cadastro.contato= contatoCadastro
            print("Aguarde registrando no banco de dados.")


            conn= pymysql.connect(db="banco",user="python",passwd="python123",host="localhost")
            time.sleep(1)
            # REGISTRANDO NO BANCO DE DADOS
            # conn= pymysql.connect(db="banco",user="python",passwd="python123",host="localhost")
            cursor = conn.cursor()
            cursor.execute("insert into cliente_poupanca(nome,cpf,contato) values('"+self.nome+"','"+self.cpf+"','"+self.contato+"')")
            # cursor.execute("insert into cadastro_clientes (nome,cpf,contato) values('"+self.nome+"', '"+self.sobrenome+"','"+self.cpf+"')")
            
            cursor.close() 
            # REGISTRANDO NO BANCO DE DADOS

            #FINALIZANDO COM PRINT:
            print("Cliente cadastrado com sucesso.")
        else:
            print("Confirmação necessaria, refaça a operação.")

#FUNÇÃO CADASTRO CLIENTE DE CREDITO
#Mesma coisa que o de cima mas com a informação extra de CEP

    def CadClienteCredito(self):

        #BLOCO 1
        #capturando info
        nomeCadastro= input("Digite o nome do cliente: ")
        cpfCadastro= input("Digite o CPF do cliente: ")
        contatoCadastro= input("Digite o contato do cliente: ")
        cepCadastro= input("Insira o CEP do cliente: ")
        statusCadastro= True


        #BLOCO 2
        #CONFIRMAÇÃO
        print(f"""Confirmação de registro:
    Nome: %s
    CPF: %s
    Contato: %s
    CEP: %s
    Aperte apenas enter para confirmar.""",(nomeCadastro,cpfCadastro,contatoCadastro,statusCadastro)) #exibindo as variaveis para confirmação)
        #CONFIRMAÇÃO


        #BLOCO 3:
        #EXECUÇÃO
        confirma= bool(input())
        if confirma== False:

            #Criando o objeto e atribuindo valor nele.
            cadastro= clienteCredito(nomeCadastro,cpfCadastro,contatoCadastro,cepCadastro,status=True)
            # cadastro.nome=(nomeCadastro)
            # cadastro.cpf=(cpfCadastro)
            # cadastro.contato(contatoCadastro)
            # cadastro.CEP(cepCadastro)
            cadastro.status(True) #Ativando a conta

            conn= pymysql.connect(db="banco",user="python",passwd="python123",host="localhost")
            time.sleep(1)
            #REGISTRANDO NO BD

            cursor = conn.cursor()
            cursor.execute('insert into cliente_credito(nome,cpf,contato,cep) values(%s,%s,%s)',(cadastro.nome,cadastro.cpf,cadastro.contato,cadastro.CEP))
            cursor.close()
            
            #finalizando ação, PRINT
            print("Cliente cadastrado com sucesso.")
        else:
            print("Confirmação necessaria, refaça a operação.")

    # def DepositoConta():
    #     idClient= int(input("Digite o ID do cliente: "))
    #     valor= float(input("Digite valor depositado: "))
        