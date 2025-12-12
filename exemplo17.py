#
# TypeVar e funções genéricas no Python moderno - Aula 8
#
# Usaremos a nova sintaxe definida pela PEP 695 (Python >=3.12)
# https://docs.python.org/3/whatsnew/3.12.html#pep-695-type-parameter-syntax

# Por este motivo:
# https://docs.python.org/3/library/typing.html#typing.TypeVar
# The preferred way to construct a type variable is via the dedicated syntax for
# generic functions, generic classes, and generic type aliases
#
# Type variable (TypeVar) é um parâmetro de tipo que atua como um símbolo para
# um tipo ainda não conhecido. Seu valor será substituído por um tipo concreto
# durante a verificação estática ou inferência de tipos.
#
# DOC: NÃO MISTURAR A VERSÃO NOVA COM A VERSÃO ANTIGA NOS SEUS TIPOS.
#
# Definições:
# `class Person[T]: ...` - O `T` significa "type parameter" ou "type variable"
# `Person[str]('John')` - O `str` entre colchete significa "type argument"
#

# Filtre um iterável por tipo. Posso ter qualquer tipo dentro do meu iterável.

from collections.abc import Iterable, Sequence

from utils import cyan_print, sep_print


def filter_by_type[T](items: Iterable[object], type_: type[T]) -> list[T]:
    return [item for item in items if isinstance(item, type_)]


def reverse_in_groups[T](items: Sequence[T], group_size: int = 2) -> list[T]:
    result: list[T] = []
    
    print(f"Items originais: {items}")
    print(f"Tamanho de items: {len(items)}")
    print(f"Group size: {group_size}\n")
    
    for index in range(0, len(items), group_size):
        print(f"--- Iteração com index = {index} ---")
        
        # Mostra o intervalo do fatiamento
        start = index
        end = index + group_size
        print(f"Fatiamento: items[{start}:{end}]")
        
        # Pega um "grupo" de items
        group = items[index : index + group_size]
        print(f"Group extraído: {group}")
        print(f"Tamanho do group: {len(group)}")
        
        # Inverte o grupo
        reversed_group = list(reversed(group))
        print(f"Group revertido: {reversed_group}")
        
        # Adiciona cada item do grupo invertido ao resultado
        for item in reversed_group:
            result.append(item)
            print(f"  Adicionando: {item} → result = {result}")
        
        print()
    
    print(f"Resultado final: {result}\n")
    return result


if __name__ == "__main__":
    sep_print()

    mixed = [1, 2, 3, "a", "b", "c", {10, 20}]
    filtered: list[set[int]] = filter_by_type(mixed, set)
    cyan_print(filtered)

    sep_print()

    reversed_groups = reverse_in_groups(mixed, group_size=2)
    cyan_print(mixed)
    cyan_print(reversed_groups)

    sep_print()
