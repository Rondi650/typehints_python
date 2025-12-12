#
# Genéricos padrão em Collections ABC
#
# Doc:
# Vídeo sobre protocolos: https://www.youtube.com/watch?v=8xnIkjROj_o
# https://docs.python.org/3/library/collections.abc.html
# https://docs.python.org/3/library/stdtypes.html#standard-generic-classes
#
# Como vimos antes, podemos usar as coleções padrão do Python para tipagem. Ou
# seja: `list[T]`, `dict[K, V]`, `tuple[T, ...]`, etc...
# Mas, isso deixa o meu código fixado no tipo escolhido. Uma função que recebe
# uma `list[str]` só pode receber `list[str]` e nada mais... E daí?
#
# Isso vai contra o Princípio da Robustez ou Lei de Postel, que diz:
#
# "Seja liberal no que você aceita, e conservador no que você retorna."
#
# Em resumo: para parâmetros que recebemos, devemos usar o tipo mais abstrato,
# enquanto nos retornos usamos valores mais restritos.
#
# Isso faz muito sentido quando você pensa em como um código funciona. Se uma
# função aceita algo que você pode percorrer (iterável), uma lista cumpre o
# papel, mas restringe todos os outros tipos que podem ser percorridos.
# Por outro lado, se uma função diz que vai retornar uma lista, o desenvolvedor
# que vai usar a função saberá os métodos que pode usar nessa lista sem quebrar
# o programa.
#
from collections.abc import Iterable, Sequence

def concat(items: Sequence[str]) -> str:
    first = items[0]
    print(f"First item: {first}")
    return "".join(items)

my_list: list[str] = ["a", "b", "c"]
my_tuple: tuple[str, ...] = ("d", "e", "f")
my_set: set[str] = {"g", "h", "i"}
my_dict: dict[int, str] = {0: "Rondinelle", 1: "k", 2: "l"}

print(f'Exemplo com Lista: {concat(my_list)}')   # OK
print(f'Exemplo com Tupla: {concat(my_tuple)}')  # OK
# print(f'Exemplo com Conjunto: {concat(my_set)}') 
print(f'Exemplo com Dicionário: {concat(list(my_dict.values()))}') 

# set
# dict
# list
