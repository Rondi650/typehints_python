from typing import Protocol

class Falante(Protocol):
    def falar(self) -> str:
        ...
        
class Pessoa:
    def falar(self) -> str:
        return "olá"
    
def comunicar(obj: Falante):
    print(obj.falar())

comunicar(Pessoa())

