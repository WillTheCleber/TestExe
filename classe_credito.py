from classe_pai import dadosCliente

#Aqui vou criar uma classe para clientes com linha de credito, ai a principal fica como conta POUPANÇA


class clienteCredito(dadosCliente):
    linhaCredito= 500

    def __init__(self, nome, cpf, contato):
        super().__init__(nome, cpf, contato)
        print("Cliente cadastrado com sucesso.")

    linhaCredito= 500
    
    def dadosExtras(self,CEP,status):
        self.CEP= CEP
        self.status= status

    #Aumento de limite com confirmação de duas etapas:
    def aumLimite(self):
        try:
            aumento= float(input("Digite a quantidade a ser aumentada no limite: "))
            conf=bool(input("""R$%s a aumentar no limite
                            Digite qualquer coisa para confirmar""",(aumento)))
            if conf == True:
                self.linhaCredito= self.linhaCredito+aumento
                print("Limite aumentado com sucesso.")
            else:
                print("Confirmação de duas etapadas obrigatorio, refaça a operação.")
        except TypeError:
            print("Digite um numero.")
        except:
            print("Erro desconhecido.")
    #metodo de compra, diminuindo o limite 
    def compra(self):
        try:
            valor= float(input("Digite o valor a ser cobrado"))
            
            test= valor-self.linhaCredito
            if test < 0:
                print("Limite insuficiente.")
            elif test>0:
                self.linhaCredito= test
            else:
                print("Erro inesperado.")
        except self.status == False:
            print("Conta desativada.")
        except TypeError:
            print("Erro digite um numero.")
        except:
            print("Erro inesperado.")
    #cancelamento de conta por pedido de cliente:

    #criei esse objeto para tentar manter o cliente
    def cancelamentoConta(self):
        print("Tem certeza que deseja cancelar o cartão?")
        conf= bool(input("- "))
        if conf == True:
            
            print("Motivo do cancelamento.")
            motiv= input('-')
            motiv.lower

            if motiv == 'limite':
                print("Ofereça um limite maior caso ele fale com gerente.(limite R$500)")
            elif motiv == 'pessoal':
                print("Ofereça um emprestimo com juros reduzidos.")

            #essa taquei confirmação de 3 etapa imaginando puramente as filas de banco
            conf2= bool(input("Última confirmação."))
            if conf2 == True:
                self.status= False
    
            
            



            
        
