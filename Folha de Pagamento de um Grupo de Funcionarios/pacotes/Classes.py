from decimal import Decimal

class Funcionario:
    
    CPF = " "
    Nome = " "
    temBonus = False
    
    def __init__(self, CPF: str, Nome: str, temBonus: bool) -> None:
        self.__CPF = CPF
        self.__Nome = Nome
        self.__temBonus = temBonus
        
    def get_Cpf(self) -> str:
            return self.__CPF
        
    def get_Nome(self,):
            return self.__Nome
        
    def set_temBonus(self, addTemBonus: str) -> None:
            self.__temBonus = addTemBonus
            
    def obterGanhos(self):
            pass

class FuncionarioHorista(Funcionario):
    
    cargaHorario = 0
    valorHora = Decimal("0")
    
    def __init__(self, CPF: str, Nome: str, temBonus: bool, cargaHorario: int, valorHora: float) -> None:
        self.cargaHorario = cargaHorario
        self.valorHora = valorHora
        self.temBonus = temBonus
        self.get_Nome = Nome
        super().__init__(CPF, Nome, temBonus) #passa para classe pai
    
    def obterGanhos(self):
        
        ganhos = self.cargaHorario * self.valorHora
        
        if self.temBonus == True:
            Bonus = (ganhos * 10) / 100
            ganhoBonus = ganhos + Bonus
            print(f"Os ganhos do funcionario horista {self.get_Nome} com bonus foi de {ganhoBonus}$") # print(f"{ganhoBonus} $") 
        elif self.temBonus == False:
            print(f"Os ganhos do funcionario horista {self.get_Nome} foi de {ganhos}$") # print(f"{ganhos} $") 
            
class FuncionarioCLT(Funcionario):
    
    salarioMensal = Decimal("0")
    
    def __init__(self, CPF: str, Nome: str, temBonus: bool, salarioMensal) -> None:
        self.salarioMensal = salarioMensal
        self.temBonus = temBonus
        self.get_Nome = Nome
        super().__init__(CPF, Nome, temBonus)
        
    def obterGanhos(self):
        
        ganhos = self.salarioMensal
        
        if self.temBonus == True:
            Bonus = (ganhos * 10) / 100
            ganhoBonus = ganhos + Bonus
            print(f"Os ganhos do funcionario contratado {self.get_Nome} com bonus foi de {ganhoBonus}$") #print(f"{ganhoBonus} $") 
        elif self.temBonus == False:
            print(f"Os ganhos do funcionario contratado {self.get_Nome} foi de {ganhos}$") #print(f"{ganhos} $") 