from abc import ABC, abstractmethod


class Funcionario(ABC):
    
    def __init__(self, nome, salario) -> None:
        self.nome = nome
        self.salario = salario
        super().__init__()
    
    def get_salario(self) -> None: ...
    
    
    @abstractmethod
    def print_name():
        ...

class Concierge(Funcionario):
    
    def __init__(self, nome, salario) -> None:
        super().__init__(nome, salario)
    
    def print_name(self):
        print(self.nome)


class Chef(Funcionario):
    
    def __init__(self, nome, salario) -> None:
        super().__init__(nome, salario)
    
    def print_name(self):
        print(self.nome)


class EmployeeFactory():
    @staticmethod
    def createEmproyee(type):
        if type == 'concierge':
            return Concierge()
        elif type == 'chef':
            return Chef()
        

funcionario = EmployeeFactory().createEmproyee(type='chef')