import datetime

class dadosCliente():
    dataCad= datetime.datetime
    saldo = 100 #atributo de classe 
    def __init__(self,nome,cpf,contato):
        self.nome=nome
        self.cpf=cpf
        self.contato=contato

    #aqui to criando a classe dos dados do cliente, chamando o construtor e definindo o self dos objetos. 

    #logo a baixo vou criar uns metodos aqui para dps tentar fazer umas interações legais. (Tenho dificuldade com polimorfismo) 
    
    #METODO DE PAGAMENTO
    def pagamento(self):
        try:
            conta= float(input("Digite a quantidade a ser paga: "))
            test =self.saldo-conta
            if test >0:
                self.saldo = self.saldo-conta
                print("Seu novo saldo é R$ %s",(self.saldo))
            else:
                print("Saldo indisponivel. ")
        except TypeError:
            print("Digite um numero. ")
        except:
            print("Erro desconhecido.")
    
    #METODO DE DEPOSITO
    def deposito(self):
        try:
            deposito= float(input("Digite a quantidade depositada: "))
            self.saldo= self.saldo+deposito
            print("Seu novo saldo é R$ %s",(self.saldo))
        except TypeError:
            print("Digite um numero.")
        except:
            print("Erro não identificado.")
    
    #METODO DE 