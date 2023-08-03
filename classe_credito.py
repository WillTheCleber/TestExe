from classe_pai import dadosCliente

#Aqui vou criar uma classe para clientes com linha de credito, ai a principal fica como conta POUPANÇA
#A ideia é separar por classes os clientes com credito e os sem. (conta poupança)




class clienteCredito(dadosCliente):
    linhaCredito= 500 #atributo de classe
    #credito pre-definido

    def __init__(self, nome, cpf, contato):
        super().__init__(nome, cpf, contato)
        print("Cliente cadastrado com sucesso.") #A base principal é a conta poupança

    
    def dadosExtras(self,CEP,status): #Dados extras para info
        self.CEP= CEP
        self.status= status #Status é a definição do credito, se está ativa (pode usar) ou  inativa (cartão bloqueado) 

    #Aumento de limite com confirmação de duas etapas:
    #Imaginando um programa manipulado por operadores criei esse metodo,
    #A ideia que achei importante é verificação de dois vatores para não aumentar 5000 ao invez de 500:
    #fiz a confirmação com variavel booleana e uma verificação de status (cartão bloqueado/desbloqueado)

    def aumLimite(self):
        try:
            #pedindo a quantidade que vai ser aumentada:
            aumento= float(input("Digite a quantidade a ser aumentada no limite: "))
            print(""""R$%s a aumentar no limite
                            Digite algo para cancelar""",(aumento))
            conf=bool(input(""))
            
            if conf == True and self.status== True:
                self.linhaCredito= self.linhaCredito+aumento
                print("Limite aumentado com sucesso.")             
            else:
                print("Confirmação de duas etapadas obrigatorio, refaça a operação.") #Bloqueio de operação caso negue o aumento.

        #FINAL DA CLASSE
        except TypeError:
            print("Digite um numero.")
        except:
            print("Erro desconhecido.")

    #metodo de compra pelo credito:
    #Segue a mesma logica do aumento de limite, só que sem confirmações, apenas reduzindo o limite:
    #pedir para o operador digitar o valor a ser "cobrado", verificar se tem credito suficiente e diminuir.
    def compra(self):
        try:
            #Variavel de pedido e variavel de test
            valor= float(input("Digite o valor a ser cobrado"))
            test= valor-self.linhaCredito

            #Execução de teste de limite (verificação)
            if test < 0:
                print("Limite insuficiente.") #limite insuficiente

            elif test>0:
                self.linhaCredito= test #Realização da compra.

            else:
                print("Erro inesperado.") #erro inesperado



        except self.status == False:
            print("Conta desativada.")
        except TypeError:
            print("Erro digite um numero.")
        except:
            print("Erro inesperado.")

    #cancelamento de conta por pedido de cliente:

    #esse metodo criei pensando num cliente querendo cancelar a conta de credito dele, ai coloquei 3 confirmações, 2 em formato bool 
    #uma de motivo (para tentar manter o cliente)

    #provavelmente NÃO VAI SER USADO NO SISTEMA (provavelmente se continuar sofrendo com coisa basica), CRIEI POR PURO TEST 
    def cancelamentoConta(self):
        #PRIMEIRA VERIFICAÇÃO.
        print("Tem certeza que deseja cancelar o cartão?")
        conf= bool(input("digite algo para cancelar:  "))#primeira verificação.


        if conf == True:
            #CAPTURA DE MOTIVO
            print("Motivo do cancelamento.")
            motiv= input('-')
            motiv= motiv.lower() #solicitando o motivo para ver se tem como manter  "QUANDO CONSEGUIR FAZER LIGAÇÃO COM DB ARMAZENAR O MOTIVO"

            if motiv == 'limite':
                print("Ofereça um limite maior caso ele fale com gerente.(limite R$500)") #famoso chá de cadeira
            elif motiv == 'pessoal':
                print("Ofereça um emprestimo com juros reduzidos.") #lucro>risco

            #essa taquei confirmação de 3 etapa imaginando puramente as filas de banco
            conf2= bool(input("enter para confirmar."))
            if conf2 == True:
                self.status= False
            else:
                print("Operação cancelada.")
        else:
            print("Operação cancelada!")

    
            
            



            
        
