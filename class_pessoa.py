class SerVivo:
    def __str__(self) -> str:
        return "Sou um ser vivo"
    
    def fazer_barulho(self) -> str:
        return "..."

class Pessoa(SerVivo):
    def __init__(self, nome: str) -> None:
        self.nome = nome
    
    def __new__(cls, nome: str):
        print(f"Classe: {cls.__name__}")
        print(f"Classe pai: {cls.__bases__}")
        return super().__new__(cls)
    
    # ✅ Chamando super() em __str__
    def __str__(self) -> str:
        pai_str = super().__str__()  # Chama SerVivo.__str__()
        return f"{pai_str} | Meu nome é {self.nome}"
    
    # ✅ Chamando super() em método normal
    def fazer_barulho(self) -> str:
        barulho_pai = super().fazer_barulho()  # Chama SerVivo.fazer_barulho()
        return f"{barulho_pai} Olá, sou {self.nome}!"
    
    def __len__(self) -> int:
        return len(self.nome)
    
    def __getitem__(self, index: int) -> str:
        return self.nome[index]

pessoa = Pessoa("Alice")
print(pessoa)
print(pessoa.fazer_barulho())
print(f'len(pessoa) = {len(pessoa)}')
print(f'pessoa[0] = {pessoa[0]}')