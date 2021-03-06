#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nombre = float(input('rentrer un nombre'))
    return abs(nombre)


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    return [prefixe+suffixes for prefixe in prefixes]


def prime_integer_summation() -> int:
    i = 0
    c = 2
    S = 0
    while i < 100:
        for j in range(c-1, 0, -1): 
            if c%j == 0:
                break
        if j == 1:
            i += 1
            S += c
        c += 1
    return S


def factorial(number: int) -> int:
    result = 1
    if number != 0:
        for i in range(number, 1, -1)
            result *= i
    return result


def use_continue() -> None:
    for entier in range(1,11)
        if entier == 5
            continue
        print(entier)


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
