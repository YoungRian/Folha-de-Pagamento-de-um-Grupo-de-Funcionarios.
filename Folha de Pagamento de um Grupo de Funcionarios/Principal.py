from pacotes import *
from decimal import Decimal
def Menu():
    print("-"*40)
    print("0 - Encerra")
    print("1 - Inserir Funcionario Horista")
    print("2 - Inserir Funcionario Contratado")
    print("-"*40)
    
lista = []
lista_horista = []

lista_contratado = []
try:
    NomeUsuario = input("Digite seu nome: ")

    while(True):
        Menu()
        try:
            HorisCont = int(input("Digite um número: "))
            
        except:
            print("Erro. Valor precisa ser igual a um número inteiro.")
        
        else:
            if HorisCont == 1:
                
                try:
                    CPF = input("Digite o CPF do funcionario: ")
                    Nome = input("Digite o nome do funcionario: ")
                except:
                    print("Erro.")
                
                try:
                    temBonus = bool(input("Tem bonus? (Para 'False' deixe o campo vazio, para 'True' digite): "))
                except:
                    print("Erro. O valor precisa ser True or False")
                    
                try:
                    cargaHorario = int(input("Digite a carga horaria do funcionario: "))
                except:
                    print("Erro. O valor da Carga Horaria tem ser igual a um número inteiro.")
                
                try:
                    valorHora = float(input("Digite o valor recebido por hora do funcionario: "))
                except:
                    print("Erro. O valor recebido por hora do funcionario tem que ser igual a float.")
                
                else:
                    lista.append(CPF)
                    lista.append(Nome)
                    lista.append(temBonus)
                    lista.append(cargaHorario)
                    lista.append(valorHora)
                
                    print("-"*45)
                
                    Ganhos_Funci_Horis = Classes.FuncionarioHorista(CPF, Nome, temBonus, cargaHorario, valorHora)
                    Ganhos_Funci_Horis.obterGanhos()
                    
                    lista_horista.append(lista)
                    
                    lista = []
                
            elif HorisCont == 2:
                try:
                    CPF = input("Digite o CPF do funcionario: ")
                    Nome = input("Digite o nome do funcionario: ")
                except:
                    print("Erro.")
                    
                try:
                    temBonus = bool(input("Tem bonus? (Para 'False' deixe o campo vazio, para 'True' digite): "))
                except:
                    print("Erro. O valor precisa ser True or False ")
                
                try:
                    salarioMensal = Decimal(input("Digite o salario mensal do funcionario: "))
                except:
                    print("Erro.")
                
                else:   
                    lista.append(CPF)
                    lista.append(Nome)
                    lista.append(temBonus)
                    lista.append(salarioMensal)
                    lista_contratado.append(lista)
                    
                    print("-"*45)
                    
                    Ganhos_Funci_Contra = Classes.FuncionarioCLT(CPF, Nome, temBonus, salarioMensal)
                    Ganhos_Funci_Contra.obterGanhos()
                    
                    lista = []

            elif HorisCont == 0:
                break
            
            else:
                print("Invalido!")

    print(" ")

    print("="*45)
    print("Funcionario Contratado") #Funcionario Contratado
    print(" ")
    for i in lista_contratado:
        print(i)
    print(" ")

    print("="*45)
    print("Funcionario Horista") #Funcionario Horista
    print(" ")
    for x in lista_horista:
        print(x)
        print(" ")
    print("="*45)

finally:
    print("Finalizado.")

